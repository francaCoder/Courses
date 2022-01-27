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