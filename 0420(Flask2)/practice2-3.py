from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def score():
   dict = {'YeHyun':70,'Gildong':50,'WoongSup':90}
   return render_template('results.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
