from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
 
#@app.route('/', methods=['GET'])
#def index():
#    return render_template('index.html', title='Form Sample')
#def index():
#  fig = Flase
#  return render_template('index.html', title='Form Sample', message='This is Jinja Template Sample', fig=fig)
#@app.route('/', methods=['GET'])
def index():
  return render_template('index.html', title='Template Sample', message='これはサンプルのページです')
#@app.route('/next', methods=['GET'])
#def next():
#  return render_template('next.html', title='Next Page', message='これは次のページのサンプルです', data=['A','B','C'])


@app.route('/', methods=['GET','POST'])
def predict():
  if request.method == 'GET':
   msg = '販売価格を予想したい住宅情報を入力して下さい'
   return render_template('predict.html', title='Predict Page', message=msg)
  
  if request.method == 'POST':
    reg = pickle.load(open('./model/trained_model.pkl', 'rb'))
    x1 = request.form['tsubo']
    x2 = request.form['tsubo_su']
    x3 = request.form['kenpei']
    x4 = request.form['building']
    x5 = request.form['age']
    x6 = request.form['birth']
    area = request.form.get('area')

    if area == 'a':
      x7 = 1
      x8 = 0
      x9 = 0
    elif area == 'b':
      x7 = 0
      x8 = 1
      x9 = 0
    elif area == 'c':
      x7 = 0
      x8 = 0
      x9 = 1
    else :
      x7 = 0
      x8 = 0
      x9 = 0
  
    x = [[int(x1), float(x2), float(x3), int(x4), int(x5), int(x6), x7 ,x8 ,x9]]
    price = reg.predict(x)
    price = price[0][0]
    price = round(price, 2)
    price = 'この住宅の予想販売価格は：{}ドルです。'.format(price)
    return render_template('predict.html', title='Predict Page', message=price, tsubo=x1, tsubo_su=x2, kenpei=x3, building=x4, age=x5, birth=x6, area=area)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)