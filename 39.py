"""". Write a program that takes a person's age and number of years of work experience as input
and prints "Entry-level" if the person is under 25 and has less than 1 year of work experience,
"Junior" if the person is between 25 and 40 and has between 1 and 5 years of work experience,
"Senior" if the person is over 40 and has between 5 and 10 years of work experience, and
"Expert" if the person is over 40 and has more than 10 years of work experience."""
age =int(input('enter the age ->'))
no_year_experience =int(input('enter the work experience-> '))
if age<25 and no_year_experience<1:
    print('entry level')
elif 25<=age<40 and no_year_experience<5:
    print('junior')
elif age>=40 and 5<=no_year_experience<10:
    print('senior')
elif age>=40 and no_year_experience>10:
    print('expert')
else:
    print('wrong,  check your input')
