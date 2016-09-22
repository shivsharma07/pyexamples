s = 'abcdeabcicdeohghu'
vowelCount = 0
for letter in s:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        vowelCount += 1
print 'Number of vowels: '+str(vowelCount)