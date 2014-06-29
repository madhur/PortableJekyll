# -*- coding: utf-8 -*-

module Handsoap
  module Http
    module Drivers
      class AbstractDriver
        def self.load!
        end

        def initialize
          self.class.load!
        end

        # Parses a raw http response into a +Response+ or +Part+ object.
        def parse_http_part(headers, body, status = nil, content_type = nil)
          if headers.kind_of? String
            headers = parse_headers(headers)
          end
          headers = headers.inject({}) {|collect,item| collect[item[0].downcase] = item[1]; collect }
          if content_type.nil? && headers['content-type']
            content_type = headers['content-type'].first
          end
          boundary = parse_multipart_boundary(content_type)
          parts = if boundary
            parse_multipart(boundary, body).map {|raw_part| parse_http_part(raw_part[:head], raw_part[:body]) }
          end
          if status.nil?
            Handsoap::Http::Part.new(headers, body, parts)
          else
            Handsoap::Http::Response.new(status, headers, body, parts)
          end
        end

        # Content-Type header string -> mime-boundary | nil
        def parse_multipart_boundary(content_type)
          if %r|\Amultipart.*boundary=\"?([^\";,]+)\"?|n.match(content_type)
            $1.dup
          end
        end

        # Parses a multipart http-response body into parts.
        # +boundary+ is a string of the boundary token.
        # +content_io+ is either a string or an IO. If it's an IO, then content_length must be specified.
        # +content_length+ (optional) is an integer, specifying the length of +content_io+
        #
        # This code is lifted from cgi.rb
        #
        def parse_multipart(boundary, content_io, content_length = nil)
          if content_io.kind_of? String
            content_length = content_io.length
            content_io = StringIO.new(content_io, 'r')
          elsif !(content_io.kind_of? IO) || content_length.nil?
            raise "Second argument must be String or IO with content_length"
          end

          boundary = "--" + boundary
          quoted_boundary = Regexp.quote(boundary, "n")
          buf = ""
          bufsize = 10 * 1024
          boundary_end = ""

          # start multipart/form-data
          content_io.binmode if defined? content_io.binmode
          boundary_size = boundary.size + "\r\n".size
          content_length -= boundary_size
          status = content_io.read(boundary_size)
          
          if nil == status
            raise EOFError, "no content body"
          elsif "\r\n" + boundary == status
            extra = content_io.read("\r\n".size)
            unless extra == "\r\n"
              raise EOFError, "parse error while reading boundary"
            end
          elsif boundary + "\r\n" != status
            raise EOFError, "bad content body"
          end

          parts = []

          loop do
            head = nil
            if 10240 < content_length
              require "tempfile"
              body = Tempfile.new("Handsoap")
            else
              begin
                require "stringio"
                body = StringIO.new
              rescue LoadError
                require "tempfile"
                body = Tempfile.new("Handsoap")
              end
            end
            body.binmode if defined? body.binmode

            until head and /#{quoted_boundary}(?:\r\n|--)/n.match(buf)

              if (not head) and /\r\n\r\n/n.match(buf)
                buf = buf.sub(/\A((?:.|\n)*?\r\n)\r\n/n) do
                  head = $1.dup
                  ""
                end
                next
              end

              if head and ( ("\r\n" + boundary + "\r\n").size < buf.size )
                body.print buf[0 ... (buf.size - ("\r\n" + boundary + "\r\n").size)]
                buf[0 ... (buf.size - ("\r\n" + boundary + "\r\n").size)] = ""
              end

              c = if bufsize < content_length
                    content_io.read(bufsize)
                  else
                    content_io.read(content_length)
                  end
              if c.nil? || c.empty?
                raise EOFError, "bad content body"
              end
              buf.concat(c)
              content_length -= c.size
            end

            buf = buf.sub(/\A((?:.|\n)*?)(?:[\r\n]{1,2})?#{quoted_boundary}([\r\n]{1,2}|--)/n) do
              body.print $1
              if "--" == $2
                content_length = -1
              end
              boundary_end = $2.dup
              ""
            end

            body.rewind
            parts << {:head => head, :body => body.read(body.size)}

            break if buf.size == 0
            break if content_length == -1
          end
          raise EOFError, "bad boundary end of body part" unless boundary_end =~ /--/
          parts
        end

        # lifted from webrick/httputils.rb
        def parse_headers(raw)
          header = Hash.new([].freeze)
          field = nil
          tmp = raw.gsub(/^(\r\n)+|(\r\n)+$/, '')
          (tmp.respond_to?(:lines) ? tmp.lines : tmp).each {|line|
            case line
            when /^([A-Za-z0-9!\#$%&'*+\-.^_`|~]+):\s*(.*?)\s*\z/om
              field, value = $1, $2
              field.downcase!
              header[field] = [] unless header.has_key?(field)
              header[field] << value
            when /^\s+(.*?)\s*\z/om
              value = $1
              unless field
                raise "bad header '#{line.inspect}'."
              end
              header[field][-1] << " " << value
            else
              raise "bad header '#{line.inspect}'."
            end
          }
          header.each {|key, values|
            values.each {|value|
              value.strip!
              value.gsub!(/\s+/, " ")
            }
          }
          header
        end
      end
    end
  end
end
