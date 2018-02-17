import stackexchange
import logging
import MySQLdb
import datetime, re, stackauth, stackexchange, stackexchange.web, unittest
import stackexchange.sites as stacksites
import rake
import operator
import sys
from stackexchange import Site, StackOverflow, Sort, DESC
from stackexchange.core import StackExchangeError
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def diskuss():
    return render_template('index.html')
    
@app.route('/node/<user>')
def node(user):

    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('home.html', user=user, recent=recent, site=site, uname=uname)
    
@app.route('/node/<user>/about/')
def about(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user;
    user = site.user(user)
    tags = user.tags.fetch()
    tag_len = len(tags)
    return render_template('about.html', user=user, tags=tags, tag_len=tag_len, uname = uname)


@app.route('/node/<user>/post/')
def post(user):
    API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
    site = stackexchange.Site(stackexchange.StackOverflow, API_KEY,  impose_throttling = True)
    uname = user
    user = site.user(user)
    recent = site.recent_questions()
    return render_template('post.html', user=user, site=site, recent=recent, uname = uname)

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
	
@app.route('/failure/')
def failure():
    return 'Sorry, please check the User ID and Password and try again later.' 

@app.route('/login',methods = ['POST'])
def login():
    user = request.form['username']
    username=user;
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="diskuss")        
    cur = db.cursor()
    cur.execute("SELECT PA FROM Password WHERE Id=%s" % user)
    data = cur.fetchone()
    if(data and data[0] == password):
        return redirect(url_for('node', user = user))
    else:
        return redirect(url_for('node', user = user))
        #redirect(url_for('failure'))


if __name__ == '__main__':
    app.run(debug = True)
