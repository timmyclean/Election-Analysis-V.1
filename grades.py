#What is the score?
score = int(input("What is the test score?"))

#Determine the grade.
if score >= 90:
    print('your grade is an A.')
elif score >= 80:
    print('your grade is a B.')
elif score >=70:
    print('your grade is C.')
elif score >= 60:
    print('your grade is D.')
else:
    print('grade is an F,')
