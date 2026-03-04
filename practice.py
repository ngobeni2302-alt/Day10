"""
1. Write a function countup_odd(n) that uses a loop to print all odd numbers from 0 up to n
(inclusive). Each number must print on its own line.
"""
def countup_odd(n):
    for i in range(0, n + 1):
        if i % 2 != 0:
            print(i)

"""
2. Write a function countdown_multiples_of_five(n) that prints all multiples of 5 from n down to 0
(inclusive). Each number must print on its own line.
"""
def countdown_multiples_of_five(n):
    for i in range(n, -1, -1):
        if i % 5 == 0:
            print(i)

"""
3. Write a function count_range(start, end) that prints numbers from start down to end (inclusive). It
should only work if start is greater than end.
"""
def count_range(start, end):
    for i in range(start, end -1, -1):
        if start > end:
            print(i)

"""
4. Write a function check_access_code(code: str) -> str that returns: 'Invalid' if empty, 'Weak' if less
than 6 characters, 'Medium' if it contains letters and numbers, and 'Strong' if it contains letters,
numbers, and symbols (!@#$). Use has_letter, has_number, and has_symbol.
"""
def check_access_code(code: str) -> str:
    if len(code) == 0:
        return "Invalid"
    if len(code) < 6:
        return "Weak"
    
    has_letter = False
    has_number = False
    has_symbol = False
    if len(code) >= 6:
        for i in code:
            if i.isalpha():
                has_letter = True
            if i.isdigit():
                has_number = True
            if i in "!@#$":
                has_symbol = True
        if has_symbol:
            return "Strong"
        else:
            return "Medium"
        
"""
5. Write a function evaluate_key(key: str) -> str that returns: 'Invalid' if empty, 'Numeric Only' if only
digits, 'Alphabet Only' if only letters, 'Alphanumeric' if letters and numbers, and 'Secure Key' if
letters, numbers, and symbols (*#&).
"""
def evaluate_key(key: str) -> str:
    if len(key) == 0:
        return "Invalid"
    if key.isdigit():
        return "Numeric Only"
    if key.isalpha():
        return "Alphabet Only"
    if key.isalnum():
        return "Alphanumeric"
    for i in key:
        if i in "*#&":
            return "Secure Key"

"""
6. Write a function check_user_password(password: str) -> str that returns: 'Invalid' if empty, 'Too
Short' if less than 8 characters, 'Basic' if it contains letters only, 'Standard' if letters and numbers,
and 'Advanced' if letters, numbers, and symbols (%$!).
"""
def check_user_password(password: str) -> str:
    if len(password) == 0:
        return "Invalid"
    if len(password) < 8:
        return "Too Short"
    if password.isalpha():
        return "Basic"
    if password.isalnum():
        return "Standard"
    for i in password:
        if i in "%$!":
            return "Advanced"
        
"""
7. Write a function reverse_sentence(sentence: str) -> str that reverses the order of the words (not
the letters) and returns the new sentence.
"""
def reverse_sentence(sentence: str) -> str:
    new_sent = sentence.split()
    new_sentence = " ".join(new_sent[::-1])
    return new_sentence

"""
8. Write a function reverse_if_long(sentence: str) -> str that reverses the sentence only if it contains
more than 4 words. Otherwise, return it unchanged.
"""
def reverse_if_long(sentence: str) -> str:

    new_sent = sentence.split()
    new_sentence = " ".join(new_sent[::-1])
    if len(new_sent) >= 4:
        return new_sentence
    else:
        return sentence

"""
9. Write a function reverse_and_uppercase(sentence: str) -> str that reverses the order of words
and converts the result to uppercase before returning it.
"""
def reverse_and_uppercase(sentence: str) -> str:
    new_sent = sentence.split()
    new_sentence = " ".join(new_sent[::-1])
    return new_sentence.upper()
