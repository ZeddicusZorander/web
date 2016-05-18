def app(environ, start_response):
    data = "\n".join(environ['QUERY_STRING'].split('&')).encode()
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response('200 OK', response_headers)
    return [data]
