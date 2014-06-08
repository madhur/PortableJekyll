module SafeYAML
  class Transform
    class ToTime
      # There isn't a missing '$' there; YAML itself seems to ignore everything at the end of a
      # string that otherwise resembles a time.
      MATCHER = /\A\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}(?:\.\d{1,5})?/.freeze

      def transform?(value)
        return false unless MATCHER.match(value)
        datetime = DateTime.parse(value) rescue nil
        if datetime.respond_to?(:to_time)
          return true, datetime.to_time
        end
        false
      end
    end
  end
end
