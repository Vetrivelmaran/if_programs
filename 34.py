"""Write a program that takes a person's blood pressure as input and prints "Normal" if the
systolic blood pressure is below 120 and the diastolic blood pressure is below 80,
"Elevated" if the systolic blood pressure is between 120 and 129 and the diastolic blood
pressure is below 80, "Stage 1 Hypertension" if the systolic blood pressure is between
130 and 139 or the diastolic blood pressure is between 80 and 89, and "Stage 2
Hypertension" if the systolic blood pressure is 140 or higher or the diastolic blood
pressure is 90 or higher"""
sbp =int(input("->"))
dbp =int(input("->"))
if sbp<120 and dbp<80:
    print('norml')
elif sbp<=129 and dbp<80:
    print('elevated')
elif sbp <=139 or dbp<=89:
    print('stage 1 hypertension')
elif sbp>=140 or sbp>=90:
    print('stage 2 hypher tension')
 