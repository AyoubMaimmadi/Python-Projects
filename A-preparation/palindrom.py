def is_palindrome(string):
    # Reverse the string and compare it to the original
    return string == string[::-1]

# Test the function
print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello"))   # Output: False


def is_palindrome(string):
    # Compare the first and last characters, then the second and second to last, and so on
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False
    return True

# Test the function
print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello"))   # Output: False
