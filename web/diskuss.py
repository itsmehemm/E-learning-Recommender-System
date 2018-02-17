from __future__ import absolute_import
from __future__ import print_function
import gensim
import pandas as pd
import xlrd
import MySQLdb
import numpy as np
import pymysql
import pyLDAvis.gensim
import pyLDAvis.graphlab
import pyLDAvis
import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt
import six
import rake
import operator
import io
import math
from textblob import TextBlob as tb
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from flask import Flask, jsonify, redirect, url_for, request, render_template
from gensim import corpora, models
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

def normalize(replies):
	min_replies = 1.0;
	max_replies = 1000.0;
	normalized_value = (float)(replies - min_replies) / (float)(max_replies - min_replies)
	return normalized_value

def tf(word, blob):
    return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
    return (float)(sum(1 for blob in bloblist if word in blob))
    
def idf(word, bloblist):
    return (float)(math.log(len(bloblist)) / (float)(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return (float)((float)(tf(word, blob)) * (float)(idf(word, bloblist)))
    
    
stoppath = "SmartStoplist.txt"
print("\n**********Welcome to diskuss Forum**********\n")
print("\nEnter User ID: ")
userid = int(input())
print("\nHave questions? Post to know the answer! :\n")
text = raw_input()
sentenceList = rake.split_sentences(text)
print("\n************************************************************")
print("Sentence-wise Split:")
for sentence in sentenceList:
    print("sentence:", sentence)
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
print("\nPhrases extracted:", phraseList)
wordscores = rake.calculate_word_scores(phraseList)
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
print("\nCandidate Keywords from the Phrases:")
for candidate in keywordcandidates.keys():
    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))
sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)
print("\nTop Keywords:")
for keyword in sortedKeywords[0:int(totalKeywords / 1)]:
    print("Keyword: ", keyword[0], ", Score: ", keyword[1])
question = text
keywords = []
for key in sortedKeywords:
	keywords.append(key[0])
print("\n************************************************************")
print("Your Question: %s " % (question))
print("Keywords: ")
print(keywords)
print("\nAdd your tag:")
mainKeyword = raw_input()
keywords.append(mainKeyword)
print("Custom tag added!")
print("Your question was successfully posted.")
print("\n************************************************************")
print("\n User Recommendation: Computing user knowledge degree")
	

answers = pd.read_excel('/home/hemm/Desktop/Final Year Project/web/Datasets/answersnew.xlsx')
degrees = []
temp_answer = []
for i in range(1, 21):
	user_answers = []
	answer_count = 0
	for j in range(0, 100):
		if(int(answers['USERID'][j]) == i and answers['DOMAIN'][j].lower() == mainKeyword.lower()):
			user_answers.append(answers['ANSWER'][j].lower())
			answer_count = answer_count + 1
	no_of_interactions = normalize(answer_count)
	# user_answers will have all answers of the users with mainKeyword; no_of_interactions will have count of answers.
	IntTema = 0
	M = []
	for j in range(0, len(keywords)):
		M.append(0)
	for j in range(0, len(user_answers)):
		for k in range(0, len(keywords)):
			M[k] = M[k] + int(user_answers[j].count(keywords[k]))
	bloblist = []
	for j in range(0, len(user_answers)):
		bloblist.append(tb(user_answers[j]))
	for blob in enumerate(bloblist):
	    #print("Top words in answer {}".format(i + 1))
	    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
	    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	    for word, score in sorted_words[:1000]:
		  if(word in keywords):
		  	#print("Word: {}, TF-IDF: {}".format(word, round(score, 10)))
		  	for i in range(0, len(keywords)):
		  		if(keywords[i] == word):
		  			key_index = i;
		  	IntTema = IntTema + score * M[key_index]
	#print("IntTema value is: %f" % IntTema)
	C = IntTema * no_of_interactions
	print("Knowledge of user %d is: " % i)
	print(C)
	degrees.append(C)

high=0.0
rec_user=0
for i in range(0, 20):
	if(degrees[i]>high):
		rec_user = i
		high = degrees[i]
		
print("User Recommended: [ %d ] with high degree of [ %f ] in [ %s ] domain" % (rec_user+1, high, mainKeyword))
print("\n************************************************************")
print("Feed Recommendations: Q&A you may like")

topics_total = 30
users_total = 4
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()
print("\nQuestions database is being read..")
questions = pd.read_excel('/home/hemm/Desktop/Final Year Project/web/Datasets/posts.xlsx')
print("\nQuestions are successfully imported.\n\n Computing Feed Recommendations..\n")
doc_set = []
for i in range(0, questions['TITLE'].size):
	doc_set.append(questions['TITLE'][i])
texts = []
for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stopped_tokens)
    #texts.append(stemmed_tokens)
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=topics_total, id2word = dictionary, passes=1)
topic = []
topic_temp = []
topic_token = []
for i in range(0, topics_total):
	topic = ldamodel.show_topic(topicid=i, topn=4)
	topic_temp.append(topic[0][0])
	topic_temp.append(topic[1][0])
	topic_temp.append(topic[2][0])
	topic_temp.append(topic[3][0])
	topic_token.append(topic_temp)
	topic_temp = []
	
similarity_matrix = []
new = []
for i in range(0, users_total):
	for j in range(0, topics_total):
		new.append(0)
	similarity_matrix.append(new)
	new = []
	
for i in range(0, users_total):
	for j in range(0, topics_total):
		for k in range(0, (questions['TITLE'].size)):
			if(questions['PARENTID'][k]-1 == i):
				for m in range(0, len(texts[k])):
					for n in range(0, len(topic_token[j])):
						if(texts[k][m] == topic_token[j][n]):
							similarity_matrix[i][j] = 1
	
topic_matrix = similarity_matrix

A =  np.array(similarity_matrix)
A_sparse = sparse.csr_matrix(A)

similarities = cosine_similarity(A_sparse)
similarities_sparse = cosine_similarity(A_sparse,dense_output=False)
vis = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)

#print(vis)
#pyLDAvis.save_html(vis, "ldaop.html")

unknown = []
temp_unknown = []
count_unknown = 0
for i in range(0, topics_total):
	if(topic_matrix[0][i]==0):
		temp_unknown.append(topic_token[i])
		unknown.append(temp_unknown)
		temp_unknown = []
		count_unknown = count_unknown + 1
		
print("\nPotential Topics of recommendations:\n")
for i in range(0, count_unknown):
	print(unknown[i])
checkbool=[]
for i in range(1, questions['TITLE'].size):
	checkbool.append(0) 
G=nx.Graph()
for i in range(0, users_total):
	for j in range(0, users_total):
		G.add_edge(i, j, weight=similarities[i][j])
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.95]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.95]
pos=nx.spring_layout(G) 
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_edges(G,pos,edgelist=elarge, width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
plt.axis('off')
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("static/images/user_graph.png") 
