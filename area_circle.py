import math


def calculate_circle():
    radius = int(input("Enter the radius of your circle: "))
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    print("The circumference is:", circumference, ", and the area is:", area)


def calculate_fat_burning_heart_rate():
    age = int(input("Enter your age in years: "))
    max_heart_rate = 206.9 - (0.67 * age)
    target = 0.65 * max_heart_rate
    print("Your target fat-burning heart rate is", target)


def greet_names():
    names = [
        "World",
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Ethan",
        "Fiona",
        "George",
        "Hannah",
        "Ian",
        "Julia",
        "Kevin",
        "Luna",
        "Mason",
        "Nora",
    ]
    for name in names:
        print(f"Hello, {name}!")


def main():
    print("1. Circle measurements")
    print("2. Fat-burning heart rate")
    print("3. Greet 15 names")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        calculate_circle()
    elif choice == "2":
        calculate_fat_burning_heart_rate()
    elif choice == "3":
        greet_names()
    else:
        print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()