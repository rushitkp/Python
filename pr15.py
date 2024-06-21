#Write a program in Python to implement read lines, write line using file handling mechanisms.

# Define a function to read lines from a file
def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

# Define a function to write lines to a file
def write_lines_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

# Define a function to append lines to a file
def append_lines_to_file(filename, lines):
    with open(filename, 'a') as file:
        file.writelines(lines)

# Read lines from a file
lines = read_lines_from_file('sample.txt')
print("Lines read from file:")
print(lines)

# Write lines to a file
new_lines = ['This is a new line\n', 'This is another new line\n']
write_lines_to_file('sample.txt', new_lines)
print("New lines written to file.")

# Append lines to a file
additional_lines = ['This is an appended line\n', 'This is another appended line\n']
append_lines_to_file('sample.txt', additional_lines)
print("Additional lines appended to file.")

# Read lines from the modified file
modified_lines = read_lines_from_file('sample.txt')
print("Modified lines read from file:")
print(modified_lines)
