#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rectangle_a = Rectangle(5, 10)
area_a = rectangle_a.calculate_area()
print(f"The area of the rectangle (Part A) is: {area_a}")

w = int(input("Enter rectangle height: "))
h = int(input("Enter rectangle weight
        : "))
rectangle_b = Rectangle(w, h)
area_b = rectangle_b.calculate_area()
print(f"The area of the rectangle (Part B) is: {area_b}")

