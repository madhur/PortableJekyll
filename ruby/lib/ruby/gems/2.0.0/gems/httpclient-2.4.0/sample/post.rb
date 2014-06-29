http = HTTPClient.new

p http.debug_dev

http.debug_dev = STDOUT
file = File.open("api_rest.pdf")
class <<file
  undef :size
end
result = http.post('http://www.google.com/', file, {"Content-Type" => 'audio/wav'})
p result
