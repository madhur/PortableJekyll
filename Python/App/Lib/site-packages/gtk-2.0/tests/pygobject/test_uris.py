import unittest

import glib

class TestUris(unittest.TestCase):
    def testExtractUris(self):
        uri_list_text = "# urn:isbn:0-201-08372-8\n" + \
                        "http://www.huh.org/books/foo.html\n" + \
                        "http://www.huh.org/books/foo.pdf\n" + \
                        "ftp://ftp.foo.org/books/foo.txt\n"
        uri_list = glib.uri_list_extract_uris(uri_list_text)
        assert uri_list[0] == "http://www.huh.org/books/foo.html"
        assert uri_list[1] == "http://www.huh.org/books/foo.pdf"
        assert uri_list[2] == "ftp://ftp.foo.org/books/foo.txt"

