"""
Make a code that read the name and two grades of several students and save all in a composite list.
At the end, show a school report with the average of each student.
Allow the user can show the grades of each student individually
"""

schoolReport = []

while True:
    name = str(input("Nome: "))
    g1 = float(input("1º Grade: "))
    g2 = float(input("2º Grade: "))
    average = (g1 + g2) / 2
    schoolReport.append([name, [g1, g2], average])

    wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        wantContinue = str(input("Do you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        break

print(" ")
print(f"{'No.':<4}{'NAME':<10}{'AVERAGE':>8}")
for index, student in enumerate(schoolReport):
    print(f"{index:<4}{student[0]:<10}{student[2]:<8.1f}")
while True:
    print("-=" * 20)
    option = int(input("Do you want to show the grades of which student? (999 to Break) "))
    if option == 999:
        print("Finishing...")
    if option <= len(schoolReport) - 1:
        print(f"Grades of {schoolReport[option][0]} are {schoolReport[option][1]}")
