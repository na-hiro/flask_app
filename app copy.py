from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html', title='INDEX', message='jinjaテンプレートを使用')

@app.route('/<id>/<password>')
def index2(id, password):
    msg = 'id: %s, password: %s' %(id, password)
    return render_template('index.html', title='INDEX', message=msg)
    
if __name__ == '__main__':
    app.debag = True
    app.run(host='localhost')
