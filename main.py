from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html> 
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body> 
    <form action="/encrypt" methods="post">
            <label>
                Rotate by:
            </label>
                <input type: "text" id="rot" name="rot" value = "0">
                <br>
                <textarea type: "text" name="text">{0}</textarea>
        <input type= "submit" value="Submit Query">
     </form>
    </body>
</html>
"""


@app.route('/', methods=['POST'])
def encrypt():
    txt = request.form['text']
    rotate = int(request.form['rot'])
    encrypt_txt = rotate_string(text, rot)
    content = encrypt_txt

    return form.format(content)

@app.route('/')
def index():
    return form.format("")

app.run()