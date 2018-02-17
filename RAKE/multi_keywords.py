from __future__ import absolute_import
from __future__ import print_function
from six.moves import range
import rake
import test_data
import sys

input_dir = sys.argv[1]

top = int(sys.argv[2])

f = open(input_dir, 'r')
text = ""
for line in f:
	text=text+line

print(text);

rake_object = rake.Rake("SmartStoplist.txt", 3, 2, 3)

keywords = rake_object.run(text)[:top]

print('RAKE keywords:', keywords)

