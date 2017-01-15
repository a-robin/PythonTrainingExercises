# Given
x = 10000.0
y = 3.0
print x / y
print 10000 / 3
# What is happening?
# Me : Rounding given the type : Integer vs double

# Given
print x - 1 / y
print (x - 1) / y
# What is happening?
# Me : Mathematical priority rule : parenthesis & division over addition

# Given 
x = 'foo'
y = 'bar'
# Create 'foobar' using x and y
# Create 'foo -> bar' using x and y
print '%s%s' % (x,y)
print '%s -> %s' % (x,y)

# Given
x = 'hello world'
# from x create 'HELLO WORLD'
# from x create 'hellX wXrld'
print '%s' % (x.upper())
print '%s' % (x.replace('o', 'X'))

# Given
x = 10000.0
y = 3.0
# print "10000 / 3 = 3333" using x and y
print '%i / %i = %i' % (x,y, x/y)

# Given
a= ['hello', 'world']
# print 'helloworld'
# print 'hello world'
# print 'hello
# world'

print '%s' % (''.join(a))
print '%s' % (' '.join(a))
print '%s' % ('\n'.join(a))

# Given
x = "Monty Python and the Holy Grail"
# create the list ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
y = "one,two,three,four"
# create the list ['one', 'two', 'three', 'four'
print '%s' % (x.split())

print '%s' % (x.split(','))