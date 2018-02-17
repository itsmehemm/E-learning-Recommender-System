from __future__ import absolute_import
from __future__ import print_function
import six
import rake as q
import operator
import io

stoppath = "SmartStoplist.txt"

ques_object = q.Rake(stoppath)

text = ""
text = raw_input("Enter your Question: ")

sentenceList = q.split_sentences(text)

for sentence in sentenceList:
    print("Sentence:", sentence)

stopwordpattern = q.build_stop_word_regex(stoppath)
phraseList = q.generate_candidate_keywords(sentenceList, stopwordpattern)
print("Phrases:", phraseList)

wordscores = q.calculate_word_scores(phraseList)

keywordcandidates = q.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print("Keyword candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))

sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
    print("Keyword: ", keyword[0], ", score: ", keyword[1])

print(ques_object.run(text))
