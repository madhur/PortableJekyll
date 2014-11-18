module Jekyll
  module Watcher
    extend self

    def watch(options)
      listener = build_listener(options)
      listener.start

      Jekyll.logger.info "Auto-regeneration:", "enabled for '#{options['source']}'"

      unless options['serving']
        trap("INT") do
          listener.stop
          puts "     Halting auto-regeneration."
          exit 0
        end

        loop { sleep 1000 }
      end
    rescue ThreadError => e
      # You pressed Ctrl-C, oh my!
    end

    def build_listener(options)
      require 'listen'
      Listen.to(
        options['source'],
        :ignore => listen_ignore_paths(options),
        :force_polling => options['force_polling'],
        &(listen_handler(options))
      )
    end

    def listen_handler(options)
      proc { |modified, added, removed|
        t = Time.now.strftime("%Y-%m-%d %H:%M:%S")
        c = modified + added + removed
        n = c.length
        print Jekyll.logger.message("Regenerating:", "#{n} files at #{t} ")
        begin
          Jekyll::Command.process_site(Jekyll::Site.new(options))
          puts  "...done."
        rescue => e
          puts "...error:"
          Jekyll.logger.warn "Error:", e.message
          Jekyll.logger.warn "Error:", "Run jekyll build --trace for more information."
        end
      }
    end

    def custom_excludes(options)
      Array(options['exclude']).map { |e| Jekyll.sanitized_path(options['source'], e) }
    end

    def to_exclude(options)
      config_files = [
        "_config.yml",
        "_config.yaml",
        "_config.toml"
      ].map { |config_file| Jekyll.sanitized_path(options['source'], config_file) }
      [config_files, options['destination'], custom_excludes(options)].flatten
    end

    # Paths to ignore for the watch option
    #
    # options - A Hash of options passed to the command
    #
    # Returns a list of relative paths from source that should be ignored
    def listen_ignore_paths(options)
      source       = Pathname.new(options['source']).expand_path
      paths        = to_exclude(options)

      paths.map do |p|
        absolute_path = Pathname.new(p).expand_path
        if absolute_path.exist?
          begin
            relative_path = absolute_path.relative_path_from(source).to_s
            unless relative_path.start_with?('../')
              path_to_ignore = Regexp.new(Regexp.escape(relative_path))
              Jekyll.logger.debug "Watcher:", "Ignoring #{path_to_ignore}"
              path_to_ignore
            end
          rescue ArgumentError
            # Could not find a relative path
          end
        end
      end.compact
    end

  end
end
