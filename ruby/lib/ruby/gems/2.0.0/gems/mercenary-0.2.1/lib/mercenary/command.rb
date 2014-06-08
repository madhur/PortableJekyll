module Mercenary
  class Command
    attr_reader :name
    attr_reader :description
    attr_reader :syntax
    attr_accessor :options
    attr_accessor :commands
    attr_accessor :actions
    attr_reader :map
    attr_accessor :parent

    # Public: Creates a new Command
    #
    # name - the name of the command
    # parent - (optional) the instancce of Mercenary::Command which you wish to
    #          be the parent of this command
    #
    # Returns nothing
    def initialize(name, parent = nil)
      @name = name
      @options = []
      @commands =  {}
      @actions = []
      @map = {}
      @parent = parent
    end

    # Public: Sets or gets the syntax string
    #
    # syntax - the string which describes this command's usage syntax (optional)
    #
    # Returns the syntax string and sets it if an argument is present
    def syntax(syntax = nil)
      @syntax = syntax if syntax
      @syntax
    end

    # Public: Sets or gets the command description
    #
    # description - the description of what the command does (optional)
    #
    # Returns the description and sets it if an argument is present
    def description(desc = nil)
      @description = desc if desc
      @description
    end

    # Public: Sets the default command
    #
    # command_name - the command name to be executed in the event no args are
    #                present
    #
    # Returns the default command if there is one, `nil` otherwise
    def default_command(command_name = nil)
      if command_name
        if commands.has_key?(command_name)
          @default_command = commands[command_name] if command_name
          @default_command
        else
          raise ArgumentError.new("'#{command_name}' couldn't be found in this command's list of commands.")
        end
      else
        @default_command
      end
    end

    # Public: Adds an option switch
    #
    # sym - the variable key which is used to identify the value of the switch
    #       at runtime in the options hash
    #
    # Returns nothing
    def option(sym, *options)
      @options << options
      @map[options[0]] = sym
    end

    # Public: Adds a subcommand
    #
    # cmd_name - the name of the command
    # block    - a block accepting the new instance of Mercenary::Command to be
    #            modified (optional)
    #
    # Returns nothing
    def command(cmd_name)
      cmd = Command.new(cmd_name, self)
      yield cmd
      @commands[cmd_name] = cmd
    end

    # Public: Add an alias for this command's name to be attached to the parent
    #
    # cmd_name - the name of the alias
    #
    # Returns nothing
    def alias(cmd_name)
      logger.debug "adding alias to parent for self: '#{cmd_name}'"
      @parent.commands[cmd_name] = self
    end

    # Public: Add an action Proc to be executed at runtime
    #
    # block - the Proc to be executed at runtime
    #
    # Returns nothing
    def action(&block)
      @actions << block
    end

    # Public: Fetch a Logger (stdlib)
    #
    # level - the logger level (a Logger constant, see docs for more info)
    #
    # Returns the instance of Logger
    def logger(level = Logger::INFO)
      unless @logger
        @logger = Logger.new(STDOUT)
        @logger.formatter = proc do |severity, datetime, progname, msg|
          "#{ident} (#{severity}): #{msg}\n"
        end
      end

      @logger.level = level
      @logger
    end

    # Public: Run the command
    #
    # argv   - an array of string args
    # opts   - the instance of OptionParser
    # config - the output config hash
    #
    # Returns the command to be executed
    def go(argv, opts, config)
      opts.banner = "Usage: #{syntax}"
      process_options(opts, config)

      if argv[0] && cmd = commands[argv[0].to_sym]
        logger.debug "Found subcommand '#{cmd.name}'"
        argv.shift
        cmd.go(argv, opts, config)
      else
        logger.debug "No additional command found, time to exec"
        self
      end
    end

    # Public: Add this command's options to OptionParser and set a default
    #         action of setting the value of the option to the inputted hash
    #
    # opts - instance of OptionParser
    # config - the Hash in which the option values should be placed
    #
    # Returns nothing
    def process_options(opts, config)
      options.each do |o|
        opts.on(*o) do |x|
          config[map[o[0]]] = x
        end
      end
    end

    # Public: Execute all actions given the inputted args and options
    #
    # argv - (optional) command-line args (sans opts)
    # config - (optional) the Hash configuration of string key to value
    #
    # Returns nothing
    def execute(argv = [], config = {})
      if actions.empty? && !default_command.nil?
        default_command.execute
      else
        actions.each { |a| a.call(argv, config) }
      end
    end

    # Public: Check if this command has a subcommand
    #
    # sub_command - the name of the subcommand
    #
    # Returns true if this command is the parent of a command of name
    # 'sub_command' and false otherwise
    def has_command?(sub_command)
      commands.keys.include?(sub_command)
    end

    # Public: Identify this command
    #
    # Returns a string which identifies this command
    def ident
      "<Command name=#{name}>"
    end

    # Public: Build a string containing the command name, options and any subcommands
    #
    # Returns the string identifying this command, its options and its subcommands
    def to_s
      msg = ''
      msg += "Command: #{name}\n"
      options.each { |o| msg += "  " + o.inspect + "\n"}
      msg += "\n"
      commands.each { |k, v| msg += commands[k].inspect }
      msg
    end
  end
end
