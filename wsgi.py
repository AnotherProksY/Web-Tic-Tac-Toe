from flaskr.server import app

if __name__ == "__main__":
    context = ('/path/to/local.crt', '/path/to/local.key')
    app.run(host='0.0.0.0', ssl_context=context)

