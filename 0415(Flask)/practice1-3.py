from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_ice(name):
    return '2016112234 서예현<br/>Hello ICE student %s!' %name

if __name__ == '__main__':
   app.run(debug=True) 
