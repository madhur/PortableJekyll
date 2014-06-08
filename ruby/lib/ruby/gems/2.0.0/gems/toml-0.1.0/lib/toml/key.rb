module TOML
  class Key
    attr_reader :key, :value
    
    def initialize(key, value)
      @key = key
      @value = value
    end
  end
end