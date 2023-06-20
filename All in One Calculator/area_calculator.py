import math

# Area calculator for 2D Figures and 3D Figures

print("1. 2D Figures")
print("2. 3D Figures")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Parallelogram")
    print("5. Rhombus")
    print("6. Triangle")
    choice_new = int(input("Enter your choice: "))
    if choice_new == 1:
        side = int(input("Enter length of the side: "))
        print(side**2)
    elif choice_new == 2:
        length = int(input("Enter length of the side: "))
        width = int(input("Enter width of the side: "))
        print(length*width)
    elif choice_new == 3:
        radius = int(input("Enter radius of the circle: "))
        print(3.14(r**2))
    elif choice_new == 4:
        pass
    elif choice_new == 5:
        pass
    elif choice_new == 6:
        pass

else:
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cone")
    print("4. Hemisphere")
    print("5. Sphere")
    print("6. Cylinder")
