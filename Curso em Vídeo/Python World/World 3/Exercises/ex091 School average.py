"""
Read the name and the average of a student, also saving the current situation in a dictionary
"""

student = {"Name": str(input("Name: ")), "Average": float(input("Average: "))}

print(f"Name → {student['Name']}")
print(f"Average → {student['Average']}")
if student['Average'] >= 6:
    print("You were approved.")
else:
    print("You were disapproved.")

# OR

student = {}
student['Name'] = str(input('Name: '))
student['Average'] = float(input(f"{student['Name']}'s average: "))
if student['Average'] >= 6:
    student['Status'] = "Approved"
else:
    student['Status'] = "Disapproved"
for k, v in student.items():
    print(f"{k} → {v}")

# OR

student = {}
student['Name'] = str(input("Name: "))
student['Average'] = float(input(f"{student['Name']}'s Average: "))
student['Status'] = "Approved" if student['Average'] >= 6 else "Disapproved"
for k, v in student.items():
    print(f"{k} → {v}")