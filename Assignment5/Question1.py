import csv
 
with open('book.csv', 'w') as file: 
    writer = csv.writer(file) 
    writer.writerow(["Name", "Address", "Email", "Mobile"])
    n = int(input("Enter number of records: "))

    for i in range(n):

        name = input("Enter name: ")
        age = input("Enter address: ")
        email = input("Enter email: ")
        mobile = input("Enter mobile: ")

        writer.writerow([name, age, email, mobile])

print("Data written successfully")