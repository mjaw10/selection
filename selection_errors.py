#test grading program

testScore = int(input("Please enter your test score: "))
if testScore >= 80:
    print("A grade")
elif testScore >= 70:
    print("B grade")
elif testScore >= 60:
    print("C grade")
elif testScore >= 50:
    print("D grade")
elif testScore >= 40:
    print("E grade")
else:
    print("Fail")
