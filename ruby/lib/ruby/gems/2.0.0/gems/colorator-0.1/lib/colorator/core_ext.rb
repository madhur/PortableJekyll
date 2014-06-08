class String
  # colorization
  def colorize(color_code)
    "\e[#{color_code}m#{self}\e[0m"
  end

  Colorator::ANSI_COLORS.each do |key, value|
    define_method(key) { colorize(value) }
  end
end