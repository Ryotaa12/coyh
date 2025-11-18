from flask import Flask
app = Flask(__name__)
@app.route('/')
def product(num1, num2):
 return num1 * num2
 print (product(2,3))
  
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)
