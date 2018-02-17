from flask import Flask, redirect, url_for, request
from linkedin import linkedin
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   API_KEY = '81mpzcy471ubsr'
   API_SECRET = 'p1sGHyX2hM6EKdpb'
   RETURN_URL = 'http://localhost:5000/success'
   authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
   print authentication.authorization_url  # open this url on your browser
   application = linkedin.LinkedInApplication(authentication)
   print application
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)

