from sys import argv

script, first, second, third = argv

first = raw_input ("How old are you?")
second = raw_input ("How tall are you?")
third = raw_input ("What are you doing?")
print "The script is called:", script
print "You are  %r years old.", first
print "You are %r tall",  second
print "You are %r",  third