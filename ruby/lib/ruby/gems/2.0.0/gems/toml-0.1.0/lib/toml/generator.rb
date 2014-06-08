
module TOML  
  class Generator
    attr_reader :body, :doc

    def initialize(doc)
      # Ensure all the to_toml methods are injected into the base Ruby classes
      # used by TOML.
      self.class.inject!
      
      @body = ""
      @doc = doc
      
      visit(@doc)
      
      return @body
    end
    
    # Whether or not the injections have already been done.
    @@injected = false
    # Inject to_toml methods into the Ruby classes used by TOML (booleans,
    # String, Numeric, Array). You can add to_toml methods to your own classes
    # to allow them to be easily serialized by the generator (and it will shout
    # if something doesn't have a to_toml method).
    def self.inject!
      return if @@injected
      require 'toml/monkey_patch'
      @@injected = true
    end
    
    def visit(hash, path = "")
      hash_pairs = [] # Sub-hashes
      other_pairs = []
      
      hash.keys.sort.each do |key|
        val = hash[key]
        # TODO: Refactor for other hash-likes (OrderedHash)
        if val.is_a? Hash
          hash_pairs << [key, val]
        else
          other_pairs << [key, val]
        end
      end
      
      # Handle all the key-values
      if !path.empty? && !other_pairs.empty?
        @body += "[#{path}]\n"
      end
      other_pairs.each do |pair|
        key, val = pair
        if key.include? '.'
          raise SyntaxError, "Periods are not allowed in keys (failed on key: #{key.inspect})"
        end
        @body += "#{key} = #{format(val)}\n"
      end
      @body += "\n" unless other_pairs.empty?
      
      # Then deal with sub-hashes
      hash_pairs.each do |pair|
        key, hash = pair
        visit(hash, (path.empty? ? key : [path, key].join(".")))
      end
    end#visit
    
    # Returns the value formatted for TOML.
    def format(val)
      val.to_toml
    end
    
  end#Generator
end#TOML
