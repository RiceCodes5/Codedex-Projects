''' Area Calculator Checkpoint Project
 This program is intended to present a menu for a user to
 choose a shape that they would like to have the area calculated.
'''
import math

shapes = ['square', 'rectangle', 'triangle', 'circle']
values = ['side', 'length', 'width', 'height', 'base', 'radius']


print("++++++++++++++++++++++++++")
print("+     Area Calculator    +")
print("++++++++++++++++++++++++++")

for indexofshapes, shape in enumerate(shapes, start=1):
    print(f'{indexofshapes}. {shape}')
userShape= input('\nPlease choose which shape you would like to know the area of.\n')


