input_user = input("Enter string to check palindrome:")

def is_palindrome(text):
    input_words = text.split()
    input_without_spaces = "".join(input_words)
    original_word = input_without_spaces.lower()
    reverse = input_without_spaces[::-1]
    palindrome_word = reverse.lower()
    
    print(input_words)
    print(input_without_spaces)
    print(original_word)
    print(reverse)
    print(palindrome_word)
    
    return original_word == palindrome_word

print(is_palindrome(input_user))


def palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(palindrome(input_user))