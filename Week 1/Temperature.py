import numpy as np

temp = np.array([18.5,19, 20, 25.0, 2, 30, 13.9])
avg_temp = np.mean(temp)

#1.Finding the Avg Temperature

print(f"Average temperature for week: {avg_temp:.2f}°C")

#2.Finding the Highest Temperature and Lowest Temperature

print(f"Highest temperature for week : {np.max(temp):.2f}°C")
print(f"Lowest temperature for week : {np.min(temp) : .2f}°C")

#3.Convert all temperatures to Fahrenheit and print the converted values.(Use the formula: F = C × 9/5 + 32)

Fahrenheit_temp = temp * 9/5 +32
print("Temperatures in Fahrenheit:")
for i in Fahrenheit_temp:
    print(f"{i:.2f}°F")

#4.Identify and print the indices of days where the temperature exceeded 20°C.

indices = np.where(temp>20)[0]
print("Indices of days where the temperature exceeded 20°C :", indices)

      

