# creating a bmi calculator
#asking for height in m
height = float(input('What is your height in m: '))
#asking for weight in kg
weight = float(input('What is your weight in kg: '))
#bmi equation
bmi = weight / height**2

print(int(bmi))