
#list of nested dictionaries example

contacts = {
    "number":4,
    "students":
    [
        {"name":"John Doe", "email":"john@example.com"},
        {"name":"Jane Doe","email":"jane@example.com"},
        {"name":"Joe Smith", "email":"joe@example.com"},
        {"name":"Stacy", "email":"stacy@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])