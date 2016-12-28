from sys import argv

script, filename = argv #unpack values two

txt = open(filename) #ready for line 8

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">") #ready for line 13

txt_again = open(file_again)

print txt_again.read()