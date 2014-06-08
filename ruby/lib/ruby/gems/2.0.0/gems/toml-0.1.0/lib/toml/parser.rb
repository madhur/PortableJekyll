module TOML  
  class Parser
    attr_reader :parsed

    def initialize(markup)
      # Make sure we have a newline on the end
      
      markup += "\n" unless markup.end_with?("\n") || markup.length == 0
      begin
        tree = Parslet.new.parse(markup)
      rescue Parslet::ParseFailed => failure
        puts failure.cause.ascii_tree
      end
      
      
      parts = Transformer.new.apply(tree) || []
      @parsed = {}
      @current = @parsed
      @current_path = ''
      
      parts.each do |part|
        if part.is_a? Key
          # If @current is an array then we're in a key-group
          if @current.is_a? Array
            # Make sure there's a table to work with.
            @current << {} if @current.last.nil?
            # Set the key on the table.
            @current.last[part.key] = part.value
            next
          end
          # Make sure the key isn't already set
          if !@current.is_a?(Hash) || @current.has_key?(part.key)
            err = "Cannot override key '#{part.key}'"
            unless @current_path.empty?
              err += " at path '#{@current_path}'"
            end
            raise err
          end
          # Set the key-value into the current hash
          @current[part.key] = part.value
        elsif part.is_a?(TableArray)
          resolve_table_array(part)
        elsif part.is_a?(Table)
          resolve_table(part)
        else
          raise "Unrecognized part: #{part.inspect}"
        end
      end
    end
    
    def resolve_table_array(t)
      @current = @parsed
      path = t.name.dup
      @current_path = path.join('.')
      while n = path.shift
        # If it's a table-array then get the last item.
        @current = @current.last if @current.is_a? Array
        
        # If it's the last item:
        if path.length == 0
          # If the current table has an item:
          if @current.has_key?(n)
            # And that item is already a table-array:
            if @current[n].is_a? Array
              # Then add an item to that table-array.
              @current[n] << {}
            else
              raise "Cannot override table array '#{t.name.join '.'}'"
            end
          else
            # Create a new table array if nothing exists here.
            @current[n] = []
          end
        elsif @current.has_key? n
          # Don't do anything if we're just moving into tables.
        else
          @current[n] = {}
        end
        @current = @current[n]
      end
    end
    
    def resolve_table(t)
      @current = @parsed

      path = t.name.dup
      @current_path = path.join('.')
      while k = path.shift
        # If it's a table-array then get the last item.
        @current = @current.last if @current.is_a? Array
        # Create a new table if one doesn't exist.
        @current[k] = {} if !@current.has_key? k
        # Move into the table.
        @current = @current[k]
      end
    end#/resolve_key_group
    
  end
end
