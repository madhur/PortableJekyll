module Mercenary
  class Program < Command
    attr_reader :optparse
    attr_reader :config

    # Public: Creates a new Program
    #
    # name - the name of the program
    #
    # Returns nothing
    def initialize(name)
      @config = {}
      super(name)
    end

    # Public: Sets or gets the program version
    #
    # version - the program version (optional)
    #
    # Returns the version and sets it if an argument is present
    def version(version = nil)
      @version = version if version
      @version
    end

    # Public: Run the program
    #
    # argv   - an array of string args (usually ARGV)
    #
    # Returns nothing
    def go(argv)
      logger.debug("Using args passed in: #{argv.inspect}")

      cmd = nil

      @optparse = OptionParser.new do |opts|
        cmd = super(argv, opts, @config)

        opts.on('-v', '--version', 'Print the version') do
          puts "#{name} #{version}"
          abort
        end
      end

      @optparse.parse!(argv)

      logger.debug("Parsed config: #{@config.inspect}")

      cmd.execute(argv, @config)
    end
  end
end
