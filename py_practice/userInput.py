def reverse(text):
    return text[::-1]
     
def isPalindrome(text):
    return text == reverse(text)
    
something = input('Enter text: ')
if(isPalindrome(something)):
    print('Yes the string is palindrome')
else:
    print('No the string is not palindrome')