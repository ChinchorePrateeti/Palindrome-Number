#create a function to check if the integer is a palindrome.
# A palindrome appears exactly same if written in a reverse order.
# example, pop, madam, 54345, **@-@**, etc

def isPalindrome(element):
    if element == element[::-1]:
        return True
    else:
        return False
    
element = input(" enter a string to check if it is a palindrome: ")
palindrome = isPalindrome(element)
print("Palindrome validity : ", palindrome)