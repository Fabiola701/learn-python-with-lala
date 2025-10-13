# menghitung bmi

name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

if bmi > 30:
    category = "Obese"
elif bmi > 25:
    category = "Overweight"
elif bmi > 18.5:
    category = "Normal weight"
elif bmi > 17:
    category = "Underweight"
else:
    category = "Severely underweight"

print(" Name:", name,"\n","BMI:", bmi,"\n","Category:", category)
# print(" Name:", name,"\n","BMI:", bmi,"\n","Category:")
# if bmi > 30:
#     print("Obese")
# elif bmi > 25:
#     print("Overweight")
# elif bmi > 25:
#     print("Overweight")
# else:
#     print("invalid input")
