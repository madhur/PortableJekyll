module TOML
  
  class Transformer < ::Parslet::Transform
    # Utility to properly handle escape sequences in parsed string.
    def self.parse_string(val)
      e = val.length
      s = 0
      o = []
      while s < e
        if val[s].chr == "\\"
          s += 1
          case val[s].chr
          when "t"
            o << "\t"
          when "n"
            o << "\n"
          when "\\"
            o << "\\"
          when '"'
            o << '"'
          when "r"
            o << "\r"
          when "0"
            o << "\0"
          else
            raise "Unexpected escape character: '\\#{val[s]}'"
          end
        else
          o << val[s].chr
        end
        s += 1
      end
      o.join
    end
    
    # Clean up arrays
    # rule(:array => subtree(:ar)) { ar.is_a?(Array) ? ar : [ar] }
    
    # Empty file
    rule('') {
      nil
    }

    # Clean up simple value hashes
    rule(:integer => simple(:i)) { i.to_i }
    rule(:float => simple(:f)) { f.to_f }
    rule(:string => simple(:s)) {
      Transformer.parse_string(s.to_s)
    }
    rule(:string => sequence(:s)) {
      raise "Unexpected string-sequence: #{s.inspect}" unless s.empty?
      ""
    }
    rule(:datetime => simple(:d)) { DateTime.iso8601(d) }
    rule(:true => simple(:b)) { true }
    rule(:false => simple(:b)) { false }
    
    rule(:key => simple(:k), :value => simple(:v)) { Key.new(k.to_s, v) }
    
    # New array cleanup
    # TODO: Make this more readable/understandable.
    def self.visit_array(h)
      if h.is_a? Hash
        # If it's an {:array => ...} hash
        a = h[:array]
        if a.is_a? Array
          # If the value is already an array
          a = a.map {|v| visit_array(v) }
          classes = a.map {|v|
            # Grab the class, with a little exception for true and false since
            # they're different classes (TrueClass and FalseClass).
            (v == true || v == false) ? true : v.class
          }
          if classes.uniq.length != 1
            raise "Conflicting types in array: " + \
              classes.map(&:to_s).join(", ")
          end
          return a
        else
          # Turn the value into an array
          return [visit_array(a)].compact
        end
      else
        # Plain old non-hash value
        return h
      end
    end
    rule(:key => simple(:k), :value => subtree(:v)) {
      Key.new(k.to_s, Transformer.visit_array(v))
    }
    
    # Make key hashes (inside key_groups) just be strings
    rule(:key => simple(:k)) { k }

    # Then objectify the key_groups
    rule(:table => simple(:kg)) {
      Table.new([kg.to_s])
    }

    # Captures array-like key-groups
    rule(:table => subtree(:kg)) {
      Table.new(kg.map &:to_s)
    }
    
    # Single name table-arrays
    rule(:table_array => simple(:name)) {
      TableArray.new([name.to_s])
    }
    # Multi-part (a.b.c) table-arrays
    rule(:table_array => subtree(:names)) {
      TableArray.new(names.map &:to_s)
    }
  end
end
