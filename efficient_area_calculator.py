#!/usr/bin/python3

from math import pi

class Area:
    @staticmethod
    def square(side):
        return side**2

    @staticmethod
    def circle(radius):
        return pi*radius**2

    @staticmethod
    def rectangle(base, height):
        return base*height

if __name__ == "__main__":

    shape_dict = {
        'square':['side'],
        'circle':['radius'],
        'rectangle':['base','height']

    }

    shape_list = ['square', 'circle', 'rectangle']
    shape_names = ""
    for i, shapes in enumerate(shape_list):
        shape_names += f'{i}. {shapes}\n'

    shape = input(f'Enter the number of the shape you want:\n{shape_names}')
    parameter_list = shape_dict[shape_list[int(shape)]]

    inputs = []
    for item in parameter_list:
       
        inputs.append(float(input(f'Enter values for {item}:  ')))


    if shape == '0':
        area = Area.square(inputs[0])

    elif shape == '2':
        area = Area.rectangle(inputs[0],inputs[1])

    print(area)

