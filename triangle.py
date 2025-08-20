def check_triangle(a, b, c):
    # First, check for triangle validity using the triangle inequality theorem
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("This is a valid triangle.")

        # Check for Equilateral triangle: all sides equal
        if a == b == c:
            print("It is an Equilateral triangle.")

        # Check for Isosceles triangle: any two sides equal
        elif a == b or b == c or a == c:
            print("It is an Isosceles triangle.")

        # Check for Right-angled triangle using Pythagoras theorem
        sides = sorted([a, b, c])
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            print("It is a Right-angled triangle.")

        # If not equilateral or right, but still valid
        if not (a == b == c) and not (a == b or b == c or a == c) and not (sides[0]**2 + sides[1]**2 == sides[2]**2):
            print("It is a Scalene triangle.")
    else:
        print("These sides do NOT form a valid triangle.")


# Example usage:
# You can change these values to test different triangles
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

check_triangle(a, b, c)
