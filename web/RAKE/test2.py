import rake
import operator
import sys
rake_object = rake.Rake("SmartStoplist.txt", 3, 5, 1)
text = raw_input()
keywords = rake_object.run(text)
print "keywords: ", keywords

