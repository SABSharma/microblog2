from app import app
@app.route('/')
@app.route ('/index')
def index():
    user={'username':'ABHISHEK'}
    return '''
<html>
<head>
<title>home page</title>
<body>
<h1>HELLO,'''+user[username]+'''!</h1>
</body>
</head>
</html>'''

