class AppModule:

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
    	data = "\n".join(self.environ['QUERY_STRING'].split('&')).encode()
    	response_headers = [
	        ('Content-type','text/plain'),
	        ('Content-Length', str(len(data)))
	    ]
    	self.start('200 OK', response_headers)
        yield data