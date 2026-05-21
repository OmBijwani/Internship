# Writing data to a file
file = open("sample.txt", "w")
file.write("Hello World\n")
file.write("Python File Handling")
file.close()


# Reading data from the file
file = open("sample.txt", "r")
print("Reading File:")
print(file.read())
file.close()


# Appending data to the file
file = open("sample.txt", "a")
file.write("\nAppending new data")
file.close()


# Reading again after appending
file = open("sample.txt", "r")
print("\nAfter Appending:")
print(file.read())
file.close()