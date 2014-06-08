module SafeYAML
  class Transform
    class ToDate
      MATCHER = /\A\d{4}\-\d{2}\-\d{2}\Z/.freeze

      def transform?(value)
        return false unless MATCHER.match(value)
        date = Date.parse(value) rescue nil
        return !!date, date
      end
    end
  end
end
