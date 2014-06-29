module Jekyll
  module Commands
    class Watch < Command
      class << self

        def init_with_program(prog)
          # noop
        end

        # Build your jekyll site
        # Continuously watch if `watch` is set to true in the config.
        def process(options)
          Jekyll.logger.log_level = :error if options['quiet']
          watch(site, options) if options['watch']
        end

        # Watch for file changes and rebuild the site.
        #
        # site - A Jekyll::Site instance
        # options - A Hash of options passed to the command
        #
        # Returns nothing.
        def watch(site, options)
          require 'listen'

          listener = Listen.to(
            options['source'],
            :ignore => ignore_paths(options),
            :force_polling => options['force_polling']
          ) do |modified, added, removed|
            t = Time.now.strftime("%Y-%m-%d %H:%M:%S")
            n = modified.length + added.length + removed.length
            print Jekyll.logger.formatted_topic("Regenerating:") + "#{n} files at #{t} "
            begin
              process_site(site)
              puts  "...done."
            rescue => e
              puts "...error:"
              Jekyll.logger.warn "Error:", e.message
              Jekyll.logger.warn "Error:", "Run jekyll build --trace for more information."
            end
          end
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
        end

      end
    end
  end
end
