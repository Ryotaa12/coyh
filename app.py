from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
 num1= 2
 num2 = 2
 product =  num1*num2
 return product
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)
