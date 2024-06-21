#Write a Python program to perform following operation on given string input:
#a) Count Number of Vowel in given string
#b) Count Length of string (donot use len() )
#c) Reverse string
#d) Find and replace operation
#e) check whether string entered is a palindrome or not


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def count_length(string):
    count = 0
    for char in string:
        count += 1
    return count

def reverse_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

def find_and_replace(string, find, replace):
    return string.replace(find, replace)

def is_palindrome(string):
    return string == string[::-1]

input_string = input("Enter a string: ")

print(f"Number of vowels: {count_vowels(input_string)}")
print(f"Length of string: {count_length(input_string)}")
print(f"Reversed string: {reverse_string(input_string)}")
find = input("Enter string to find: ")
replace = input("Enter string to replace: ")
print(f"String after find and replace: {find_and_replace(input_string, find, replace)}")
print(f"Is the string a palindrome? {is_palindrome(input_string)}")
