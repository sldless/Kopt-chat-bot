from flask import Flask, render_template, request
import requests as rqts
app = Flask(__name__)
import random
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        msg = request.form["msg"]
    except:
        msg = 'Hello would'
        for i in msg:
            msg = i
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if msg.find(random.choice(abc)):
        msg.replace(random.choice(abc), random.choice(abc))
        
    chat = rqts.get(
        f'https://api.pgamerx.com/ai/response?message={msg}&language=english')
    content = {
        'reply': str(chat.json()[0])
    }
    return render_template('index.html', **content)

if __name__ == '__main__':
    app.run(debug=True)
