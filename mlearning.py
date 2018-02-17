import pandas as pd
import xlrd
import MySQLdb
import pymysql

posttags = pd.read_excel('/home/hemm/Desktop/Final Year Project/Datasets/PostTags.xlsx')

posts = pd.read_excel('/home/hemm/Desktop/Final Year Project/Datasets/Posts.xlsx')

tags = pd.read_excel('/home/hemm/Desktop/Final Year Project/Datasets/Tags.xlsx')

votes = pd.read_excel('/home/hemm/Desktop/Final Year Project/Datasets/Votes.xlsx')

merge_inner = pd.merge(left=tags,right=posttags, left_on='Id', right_on='TagId')

merge_inner = pd.merge(left=merge_inner, right=posts, left_on='PostId', right_on='ParentId')

votes_new = votes[votes.VoteTypeId == 5]

merge_inner = pd.merge(left=merge_inner, right=votes_new, left_on='Id_y', right_on='PostId')

print merge_inner;


