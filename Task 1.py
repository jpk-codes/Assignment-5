name_mark = {'Alice' : 85, 'Arun' : 97, 'Pran' : 98, 'Sree' : 90}
name = input("Enter the student's name: ")
name = name.capitalize()
if name in name_mark:
    print(name + "'s marks:", name_mark[name])
else:
    print("Student not found.")
