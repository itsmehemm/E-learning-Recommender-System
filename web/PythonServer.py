import stackexchange
import logging
import MySQLdb
import datetime, re, stackauth, stackexchange, stackexchange.web, unittest
import stackexchange.sites as stacksites
import rake
import openpyxl
import operator
import sys
import xlrd
import codecs
import xlwt
from xlutils.copy import copy
from stackexchange import Site, StackOverflow, Sort, DESC
from stackexchange.core import StackExchangeError
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def diskuss():
    return render_template('index.html')
    
@app.route('/node/<user>/topstories')
def topstories(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('topstories.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/postsuccess', methods = ['POST', 'GET'])
def postsuccess(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    question = request.form['question']
    print("Question posted:")
    print(question)
    rb = xlrd.open_workbook('Datasets/posts.xls',formatting_info=True)
    r_sheet = rb.sheet_by_index(0) 
    r = r_sheet.nrows
    print("rows:")
    print(r)
    wb = copy(rb) 
    sheet = wb.get_sheet(0) 
    sheet.write(r,1,uname)
    sheet.write(r,3,question)
    sheet.write(r,0,"")
    sheet.write(r,2,"")
    wb.save('Datasets/posts.xls')
    return redirect(url_for('feed', user = uname))

@app.route('/node/<user>/feed')
def feed(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('home.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/post/')
def post(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('post.html', user=user, site=site, recent=recent, uname = uname)

@app.route('/node/<user>/answer')
def answer(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('answer.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/notifications')
def notifications(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('notifications.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/requests')
def requests(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('requests.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/about/')
def about(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    tags = user.tags.fetch()
    tag_len = len(tags)
    return render_template('about.html', user=user, tags=tags, tag_len=tag_len, uname = uname)

@app.route('/node/<user>/diskuss')
def aboutdiskuss(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('aboutdiskuss.html', user=user, recent=recent, site=site, uname=uname)


@app.route('/node/<user>/process/', methods = ['POST', 'GET'])
def process(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user
    user = site.user(user)
    question=request.form['question']
    rake_object = rake.Rake("SmartStoplist.txt", 3, 5, 1)
    keywords = rake_object.run(question)
    print "keywords: ", keywords
    recent = site.recent_questions()
    return render_template('postfinal.html', user=user, site=site, keywords=keywords, question=question, recent=recent, uname = uname)

@app.route('/node/<user>/processfeedback/', methods = ['POST', 'GET'])
def processfeedback(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user
    user = site.user(user)
    username=request.form['username']
    email=request.form['email']
    feedback=request.form['feedback']
    rb = xlrd.open_workbook('feedback.xls',formatting_info=True)
    r_sheet = rb.sheet_by_index(0) 
    r = r_sheet.nrows
    wb = copy(rb) 
    sheet = wb.get_sheet(0) 
    sheet.write(r,0,username)
    sheet.write(r,1,email)
    sheet.write(r,2,feedback)
    wb.save('feedback.xls')
    return render_template('feedbacksuccess.html', user=user, site=site, uname = uname)

@app.route('/node/<user>/contact')
def contact(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('contact.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/feedback')
def feedback(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('feedback.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/recommendation')
def recommendation(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('recommendation.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/node/<user>/lda')
def lda(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('ldaop.html')

@app.route('/node/<user>/favorite/')
def fav(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    user = site.user(user)
    fav = user.favorites.fetch()
    return render_template('fav.html', user=user, fav=fav, site=site)


@app.route('/node/<id>/reputation/')
def reputation(id):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    user = site.user(id)
    recent = site.recent_questions()
    
    return render_template('details.html', uname=user.displayname, recent=recent);
	
@app.route('/node/<user>/graph')
def graph(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('graph.html', user=user, recent=recent, site=site, uname=uname)

@app.route('/failure/')
def failure():
    return 'Sorry, please check your User ID and Password and try again later.'

@app.route('/notfound/')
def notfound():
    return 'Sorry, this page is still under construction.' 

@app.route('/login',methods = ['POST'])
def login():
    user = request.form['username']
    username=user;
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="diskuss")        
    cur = db.cursor()
    cur.execute("SELECT Pass FROM Password WHERE Id=%s" % user)
    data = cur.fetchone()
    if(data and data[0] == password):
        return redirect(url_for('topstories', user = user))
    else:
        return redirect(url_for('topstories', user = user))
        #redirect(url_for('failure'))

if __name__ == '__main__':
    app.run(debug = True)
