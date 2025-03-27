''' Area Calculator Checkpoint Project
 This program is intended to present a menu for a user to
 choose a shape that they would like to have the area calculated.
 It's inspired by multiple dispatch in Julia, we just learned about it in my programming language theory class.
 Definitely easier in Julia lol
'''
import math

shapes = ['square', 'rectangle', 'triangle', 'circle', 'exit']
shapeInputs = {
    'square' : ['side'],
    'rectangle' : ['length', 'width'],
    'triangle' : ['height', 'base'],
    'circle' : ['radius']
}

print("++++++++++++++++++++++++++")
print("+     Area Calculator    +")
print("++++++++++++++++++++++++++")
print()

while True:

    for indexofshapes, shape in enumerate(shapes, start=1):
        print(f'\n{indexofshapes}. {shape}')
    userShape= input('\nPlease choose which shape you would like to know the area of. ').strip().lower()

    if userShape == 'exit' or userShape == '5':
        print("\nGoodbye!")
        break

    elif userShape == 'square' or userShape == '1':
        userInput = {}
        for areaofsq in shapeInputs['square']:
            userInput[areaofsq] = float(input(f"\nWhat is the size of the square's side? "))
        area = userInput['side'] ** 2
        print(f'\n The area of your square is {area}')

    elif userShape == "rectangle" or userShape == '2':
        userInput = {}

        for areaofrect in shapeInputs['rectangle']:
            userInput[areaofrect] = float(input(f"\nWhat is the size of the {areaofrect} of the rectangle? "))
        area = userInput['length'] * userInput['width']
        print(f'\n The area of your rectangle is {area}')

    elif userShape == "triangle" or userShape == "3":
        userInput = {}
        for areaoftriangle in shapeInputs['triangle']:
            userInput[areaoftriangle] = float(input(f"\nWhat is the size of the triangle's {areaoftriangle}? "))
        area = userInput['height'] * userInput['base'] / 2
        print(f'\n The area of your triangle is {area}')

    elif userShape == "circle" or userShape == "4":
        userInput = {}
        for areaofcircle in shapeInputs['circle']:
            userInput[areaofcircle] = float(input(f"\nWhat is the size of the circle's {areaofcircle}? "))
        area = userInput['radius'] ** 2 * math.pi
        print(f"\n The area of your circle is {area:.2f}")

    else:
        print("\nSorry, please input a valid option.\n")
        continue

    again = input("\nWould you like to calculate another area? (yes/no): ").strip().lower()
    if again != 'yes':
        print("\nThanks for using the Area Calculator. Goodbye!")
        break




