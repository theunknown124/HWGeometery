# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.
import circle
import rectangle

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while choice != 5:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input("Enter your choice: "))

        # Perform the selected action.
        if choice == 1:
            radius = float(input("Enter the circle's radius: "))
            print('The area is', circle.calcAreaOfCircleforRadius(radius))
        elif choice == 2:
            radius = float(input("Enter the circle's radius: "))
            print("The circumference is ", circle.calcCircumference(radius))
        elif choice == 3:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The area of the rectangle is ", rectangle.areaOfRectangle(width,length))
        elif choice == 4:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The perimeter of the rectangle is ", rectangle.calcPerimeter(width,length))


        elif choice == 5:
            print("Exiting the program")

        else:
            print('Error: invalid selection.')


# The display_menu function displays a menu.
def display_menu():
    print("\nEnter the  for desired option: ")
    print("1. Area of Circle")
    print("2. Circumference of the circle")
    print("3. Area of a rectangle")
    print("4. Perimeter of a rectangle")
    print("5. Quit")


# Call the main function.
if __name__ == "__main__":
    main()