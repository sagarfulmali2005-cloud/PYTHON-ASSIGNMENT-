# open file
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This is file handling example.\n")
file.close()

# Read the file
file = open("sample.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

# Append to the file    
file = open("sample.txt", "a")
file.write("This line is appended later.\n")
file.close()

# Read the file again to see the changes
file = open("sample.txt", "r")
print("Updated Content:\n", file.read())
file.close()

