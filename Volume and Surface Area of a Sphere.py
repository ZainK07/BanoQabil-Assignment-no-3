# Write a program that prompts the user to enter a radius and then calculates the volume and surface area of a sphere. The formulas for volume and surface area are V = (4/3) _ pi _ r^3 and A = 4 _ pi _ r^2, respectively.

Radius=float(input("Enter The Radius"))
pi=3.142
Volume_Of_The_Sphere=(4/3)*pi*Radius**3
Surface_Area_Of_A_Sphere=4*pi*Radius**2
print("The Volume Of The Sphere Is", Volume_Of_The_Sphere)
print("The Surface Area Of A Sphere Is", Surface_Area_Of_A_Sphere)
