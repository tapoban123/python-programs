# Write a program that calculates and displays the volume of sphere, cylinder, cube
# and cone, based on user input. Define a function for each shape, using default
# values for some of the arguments (e.g., radius, length).

import math


def volOfSphere(radius):
    return (4 / 3) * math.pi * radius**3


def volOfCone(radius, height):
    return (1 / 3) * math.pi * radius**2 * height


def volOfCylinder(radius, height):
    return math.pi * radius**2 * height


def volOfCube(side):
    return side**3


def menu():
    print("Enter 1 to find the volume of sphere.")
    print("Enter 2 to find the volume of cone.")
    print("Enter 3 to find the volume of cylinder.")
    print("Enter 4 to find the volume of cube.")


def main():
    menu()
    while True:
        userChoice = int(input("Enter your choice: "))
        if userChoice == 1:
            radius = float(input("Enter the radius: "))
            print(f"Volume of Sphere = {volOfSphere(radius)}")
        
        elif userChoice == 2:
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))
            print(f"Volume of Cone = {volOfCone(radius, height)}")

        elif userChoice == 3:
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))
            print(f"Volume of Cylinder = {volOfCylinder(radius, height)}")

        elif userChoice == 4:
            side = float(input("Enter length of one side: "))
            print(f"Volume of Cube = {volOfCube(side)}")

        else:
            print("Program Executed.")
            break

main()