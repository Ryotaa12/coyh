from flask import Flask
app = Flask(__name__)
@app.route('/')
 num1= 2
 num2 = 2
 product = multiply (num1, num2)
 print ( product )
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)
