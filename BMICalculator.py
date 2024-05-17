#Name: Nasser Binmarzook
#ID: 60306933
#Course&Section: INFS 1101-4
#Lab 5
weight = input("Input your weight in KG: ")
height = input("Input your height in meters: ")
weight = float(weight)
height = float(height)
BMI = weight / (height**2)
#Healthy weight at BMI = 23:
hweight = 23 * (height**2)
lossGain = abs(weight-hweight)
print(f"Your BMI is {BMI} kg/m")
if BMI < 20:
    print("You are underweight.")
    print(f"You need to gain {lossGain} kg.")
    print(f"Your goal weight should be around {hweight} kg")
elif BMI >= 20 and BMI < 25:
    print("Your weight is healthy.")
elif BMI >= 25 and BMI < 30:
    print("You are overweight.")
    print(f"You need to lose {lossGain}.")
    print(f"Your goal weight should be {hweight}")
elif BMI >= 30 and BMI < 40:
    print("You are obese.")
    print(f"You need to lose {lossGain} kg.")
    print(f"Your goal weight should be around {hweight}")
else:
    print("You are morbidly obese")
    print("Consult your doctor IMMEDIETLY!!!")
    print(f"You need to lose {lossGain} kg.")
    print(f"Your goal weight should be around {hweight} kg.")
print("Have a good day!")