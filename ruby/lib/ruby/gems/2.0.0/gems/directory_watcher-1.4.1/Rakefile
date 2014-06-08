
begin
  require 'bones'
rescue LoadError
  abort '### please install the "bones" gem ###'
end

Bones {
  name         'directory_watcher'
  summary      'A class for watching files within a directory and generating events when those files change'
  authors      'Tim Pease'
  email        'tim.pease@gmail.com'
  url          'http://gemcutter.org/gems/directory_watcher'
  ignore_file  '.gitignore'

  depend_on  'bones-git',    :development => true
  depend_on  'rev',          :development => true
  depend_on  'eventmachine', :development => true
}

