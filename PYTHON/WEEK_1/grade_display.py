print("Enter the 4 subject marks")
marks1 = int(input(">"))
marks2 = int(input(">"))
marks3 = int(input(">"))
marks4 = int(input(">"))
avg = (marks1 + marks2 + marks3 + marks4) / 4
if 90 < avg <= 100:
    print("S grade")
elif 80 < avg <= 90:
    print("A grade")
elif 70 < avg <= 80:
    print("B grade")
elif 60 < avg <= 70:
    print("C grade")
elif 50 < avg <= 60:
    print("D grade")
elif 40 <= avg <= 50:
    print("E garde")
else:
    print("F grade")

