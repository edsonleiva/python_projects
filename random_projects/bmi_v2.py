###### BMI Version 2 ######

#asking for height in m
height = float(input('What is your height in m: '))
#asking for weight in kg
weight = float(input('What is your weight in kg: '))
#bmi equation
bmi = round(weight / height**2)

#Checks to see which BMI value is represented by the BMI calculator
if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese.')
elif bmi >= 35:
    print(f'Your BMI is {bmi}, you are clinically obese.')
else:
    print('We are sorry there seems to be an error...')