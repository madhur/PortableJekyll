# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "maruku"
  s.version = "0.7.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Andrea Censi", "Nathan Weizenbaum", "Ben Hollis"]
  s.cert_chain = ["-----BEGIN CERTIFICATE-----\nMIIDbDCCAlSgAwIBAgIBATANBgkqhkiG9w0BAQUFADA+MQwwCgYDVQQDDANiZW4x\nGTAXBgoJkiaJk/IsZAEZFgliZW5ob2xsaXMxEzARBgoJkiaJk/IsZAEZFgNuZXQw\nHhcNMTMwMzExMDI1NTUzWhcNMTQwMzExMDI1NTUzWjA+MQwwCgYDVQQDDANiZW4x\nGTAXBgoJkiaJk/IsZAEZFgliZW5ob2xsaXMxEzARBgoJkiaJk/IsZAEZFgNuZXQw\nggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC5zj8rp/43ROFWTrOmaXFI\nsaYRkgYgv5y0+10/MRZDPYT3i42GRmCPRd+ZWAVPKGJCRgSizgAfPSYh8+CFceFm\nZVzeTd5haVWgsSkLpDHc3CuIUnanEOhlLcNt7bjofoxiZaqMm8ntLGAPARunOn4H\nwhN7a82KEMRYCqC0H1TvTR15K7Fb40U6UgrqwiaQtDvTyIALakzICl2mBk5we3La\nOAgoKVT0SDAUa8E4BSitpOpukNTPPy7r0WKb8yO69ON19LGxg17tDJjolKYsScOt\n+nXZj7HJwfBkn9m6zxDqCk7mvAvybH7oMOCzrxLB9kxSOjNOCVnOV26Bj5xPUY8p\nAgMBAAGjdTBzMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgSwMB0GA1UdDgQWBBTXpLoI\nloLWXfgQPVg/t4cAuHJZeDAcBgNVHREEFTATgRFiZW5AYmVuaG9sbGlzLm5ldDAc\nBgNVHRIEFTATgRFiZW5AYmVuaG9sbGlzLm5ldDANBgkqhkiG9w0BAQUFAAOCAQEA\nCYVy5TtuDMQz7ddO+bc+Jve9V6o1Fpu6bXTlwsXafXtfOeJ3/+0g+WboTCbCWjIR\nJnPcE2vCVrLF48PpR3YWVRGZai4YxRXdmZEcVDnJReymUHVu0hZdcxV6+LecoZ5a\nX06W7WI+JhEKb5zIgGFGuW074n0el0il85NI/frb9D3dOKqU5+NK7hrRO8rjWLXo\nU+KBnqpu0lI1TIAshS1R8JYVLIixEg6sl3+QljvpDQW+P4D1qg6wspdjKj91/geA\nKwEyUbH6HjXBdbfv95jHa8ncuWqIryt/ywGZg3sbPVsscZA9RcyDtUQRnlHSGRWH\nZSsIzVZvxIwTYa0z3d+JWQ==\n-----END CERTIFICATE-----\n"]
  s.date = "2013-09-28"
  s.description = "Maruku is a Markdown interpreter in Ruby.\n\tIt features native export to HTML and PDF (via Latex). The\n\toutput is really beautiful!"
  s.email = "ben@benhollis.net"
  s.executables = ["maruku", "marutex"]
  s.files = ["bin/maruku", "bin/marutex"]
  s.homepage = "http://github.com/bhollis/maruku"
  s.licenses = ["MIT"]
  s.require_paths = ["lib"]
  s.required_ruby_version = Gem::Requirement.new(">= 1.8.7")
  s.rubygems_version = "2.0.3"
  s.summary = "Maruku is a Markdown-superset interpreter written in Ruby."
end
