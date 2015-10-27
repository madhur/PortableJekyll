require 'cgi'
require 'net/http'

Net::OpenTimeout = Class.new(RuntimeError) unless Net.const_defined?(:OpenTimeout)
Net::ReadTimeout = Class.new(RuntimeError) unless Net.const_defined?(:ReadTimeout)

module Jekyll
  module Gist
    class GistTag < Liquid::Tag

      def render(context)
        @encoding = context.registers[:site].config['encoding'] || 'utf-8'
        if tag_contents = determine_arguments(@markup.strip)
          gist_id, filename = tag_contents[0], tag_contents[1]
          if context.has_key?(gist_id)
            gist_id = context[gist_id]
          end
          if context.has_key?(filename)
            filename = context[filename]
          end
          noscript_tag = gist_noscript_tag(gist_id, filename)
          script_tag = gist_script_tag(gist_id, filename)
          "#{noscript_tag}#{script_tag}"
        else
          raise ArgumentError.new <<-eos
  Syntax error in tag 'gist' while parsing the following markup:

    #{@markup}

  Valid syntax:
    {% gist user/1234567 %}
    {% gist user/1234567 foo.js %}
    {% gist 28949e1d5ee2273f9fd3 %}
    {% gist 28949e1d5ee2273f9fd3 best.md %}
  eos
        end
      end

      private

      def determine_arguments(input)
        matched = input.match(/\A([\S]+|.*(?=\/).+)\s?(\S*)\Z/)
        [matched[1].strip, matched[2].strip] if matched && matched.length >= 3
      end

      def gist_script_tag(gist_id, filename = nil)
        url = "https://gist.github.com/#{gist_id}.js"
        url = "#{url}?file=#{filename}" unless filename.empty?
        "<script src=\"#{url}\"> </script>"
      end

      def gist_noscript_tag(gist_id, filename = nil)
        code = fetch_raw_code(gist_id, filename)
        if !code.nil?
          code = code.force_encoding(@encoding)
          "<noscript><pre>#{CGI.escapeHTML(code)}</pre></noscript>"
        else
          Jekyll.logger.warn "Warning:", "The <noscript> tag for your gist #{gist_id} could not"
          Jekyll.logger.warn "", "be generated. This will affect users who do not have"
          Jekyll.logger.warn "", "JavaScript available or enabled in their browsers."
        end
      end

      def fetch_raw_code(gist_id, filename = nil)
        url = "https://gist.githubusercontent.com/#{gist_id}/raw"
        url = "#{url}/#{filename}" unless filename.empty?
        begin
          uri = URI(url)
          Net::HTTP.start(uri.host, uri.port,
            use_ssl: uri.scheme == 'https',
            read_timeout: 3, open_timeout: 3) do |http|
            request = Net::HTTP::Get.new uri.to_s
            response = http.request(request)
            response.body
          end
        rescue SocketError, Net::HTTPError, Net::OpenTimeout, Net::ReadTimeout, TimeoutError
          nil
        end
      end
    end
  end
end

Liquid::Template.register_tag('gist', Jekyll::Gist::GistTag)
