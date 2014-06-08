# enable RubyInstaller DevKit usage as a vendorable helper library
unless ENV['PATH'].include?('D:\\PortableJekyll\\x86\\devkit\\mingw\\bin') then
  phrase = 'Temporarily enhancing PATH to include DevKit...'
  if defined?(Gem)
    Gem.ui.say(phrase) if Gem.configuration.verbose
  else
    puts phrase
  end
  puts "Prepending ENV['PATH'] to include DevKit..." if $DEBUG
  ENV['PATH'] = 'D:\\PortableJekyll\\x86\\devkit\\bin;D:\\PortableJekyll\\x86\\devkit\\mingw\\bin;' + ENV['PATH']
end
ENV['RI_DEVKIT'] = 'D:\\PortableJekyll\\x86\\devkit'
ENV['CC'] = 'gcc'
ENV['CXX'] = 'g++'
ENV['CPP'] = 'cpp'
