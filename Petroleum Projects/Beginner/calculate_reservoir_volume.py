# Calculate Reservoir Volume

print("Select shape of the reservoir from the below list")
print("Enter values in meters")
print("1. Cylindrical")
print("2. Rectangular")
print("3. Conical")
print("4. Spherical")

choice = int(input("Enter a choice: "))

# Variables to use
pi = 3.14

if choice == 1:
    r = int(input("Enter radius of the cylindrical reservoir: "))
    h = int(input("Enter height of the cylindrical reservoir: "))
    v = pi*(r**2)*h
    print("Volume of the reservoir is", v)

elif choice == 2:
    l = int(input("Enter length of the rectangular reservoir: "))
    w = int(input("Enter width of the rectangular reservoir: "))
    h = int(input("Enter height of the rectangular reservoir: "))

    v = l * w * h
    print("Volume of the reservoir is", v)

elif choice == 3:
    r = int(input("Enter radius of the conical reservoir: "))
    h = int(input("Enter height of the conical reservoir: "))

    v = (1/3)*pi*(r**2)*h
    print("Volume of the reservoir is", v)

elif choice == 4:
    r = int(input("Enter radius of the spherical reservoir: "))

    v = (4/3)*pi*(r**3)
    print("Volume of the reservoir is", v)


