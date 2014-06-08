module TOML
  class Table
    # :name is array of strings
    attr_reader :name
    def initialize(name)
      @name = name
    end
  end
  class TableArray < Table; end
end
