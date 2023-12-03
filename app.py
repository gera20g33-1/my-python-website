from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask

app = Flask(__name__)

def hello():
    name = input("What's your name?")
    put_text("Hello,", name)

app.add_url_rule('/hello', 'webio_view', webio_view(hello),
            methods=['GET', 'POST', 'OPTIONS'])
app.run()
