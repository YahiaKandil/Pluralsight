
contacts = {
    "Number": 4,
    "Students":[
        {"Name":"Yahia", "Email":"yahiakandil@outlook.com"},
        {"Name":"Ali", "Email":"ali@outlook.com"},
        {"Name":"Nick", "Email":"nick@outlook.com"},
        {"Name":"James", "Email":"James@outlook.com"},
        {"Name":"Kevin", "Email":"Kevin@outlook.com"}
    ]
}

# Print the emails of students

for student in contacts["Students"]:
    print("\n" + student["Email"])
