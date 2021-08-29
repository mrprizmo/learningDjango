def app(environ, start_response):
    data = [bytes(line + '\n', 'ascii') for line in environ["QUERY_STRING"].split('&')]
    start_response("200 OK", ("Content-Type", "text/plain"))
    return iter(data)