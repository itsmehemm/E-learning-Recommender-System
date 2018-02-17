import stackexchange
from stackexchange import Site, StackOverflow, Sort, DESC
import logging
import datetime, re, stackauth, stackexchange, stackexchange.web, unittest
import stackexchange.sites as stacksites
from stackexchange.core import StackExchangeError


API_KEY = ")e55ob6fBvCtSTibWPyP*A(("
so = stackexchange.Site(stackexchange.StackOverflow, API_KEY, impose_throttling = True)

you = so.user(1000)
#badges = you.tags.top_questions
#print badges
#print "next"
#pre = you.answers.fetch(pagesize=60)
#for answer in pre:
#	print answer.score;

print you.account_id	
print you.creation_date
print you.display_name
print you.last_access_date
print you.location
reputation_detail = you.reputation_detail.fetch()
print reputation_detail
#print(you.display_name)
#print(you.website_url)
#print(you.location)
#print(you.top_answer_tags.fetch())
#print(you.id);
#print(you.top_question_tags.fetch())
#print(you.reputation.format())
#total_questions = len(you.questions.fetch())
#print(you.creation_date)
#print(you.last_access_date)
#print(you.questions.fetch()[0])

#unaccepted_questions = len(you.unaccepted_questions.fetch())
#accepted = total_questions - unaccepted_questions
#rate = accepted / float(total_questions) * 100
#print('Accept rate is %.2f%%.' % rate)
