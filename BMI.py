user_weight = float(input("enter your body weight in kg  "))
user_height = float(input("enter your height in meters "))
bmi = user_weight / (user_height ** 2)
user_bmi = round(bmi ,2)
print(f"your BMI is {user_bmi}")
if user_bmi < 18.8:
    print("you are underweight ")
elif 18.8 <= user_bmi <= 24.9:
    print("you are healthy weight ")
elif 24.9 < user_bmi <= 39.9:
    print("you are overweight ")
else:
    print(" you are obese ")