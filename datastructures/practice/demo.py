'''
Created on Apr 15, 2015

@author: Shiv Sharma
'''

name = 'Shiv'
email = 'shiv@gmail.com'
question = r"What's your name? \n\
second sentence"
print (question)

tripleQuoteString = '''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

print (tripleQuoteString)

print ("Name : {} Email: {}".format(name,email))

print ('{0:.5}'.format(4.0//3)) #floor division

print ('{name} wrote {book}'.format(name='Shiv', book='Meluha'))

print ('hello '*5)

print (5&3)


l1 = [57,6,88,9,68]
print (l1[0:-1])

#l1.sort()
print (sorted(l1))

l1.remove(88)
del(l1[2])
l1.pop() #l1.pop(1)

l1.append(28)
l1.insert(1, 57)
