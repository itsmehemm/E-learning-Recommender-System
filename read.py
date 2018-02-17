import pandas as pd
import xlrd
import MySQLdb
import pymysql
from flask import Flask, jsonify, redirect, url_for, request, render_template

table = pd.read_excel('/home/hemm/Desktop/Final Year Project/posts.xlsx')
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="diskuss")        
cur = db.cursor()
sql = """INSERT INTO SAMPLE VALUES(%d,"%s")""" % (table['Id'][0], table['Body'][0])
cur.execute(sql);
		
