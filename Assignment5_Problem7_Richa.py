#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Triangle:
    def __init__(self, base, perpendicular):
        self.base = base
        self.perpendicular = perpendicular

    def calculateHypotenuse(self):
        base_squared = self.base ** 2
        perpendicular_squared = self.perpendicular ** 2
        return (base_squared + perpendicular_squared) ** 0.5

base = float(input("Enter the base of the triangle: "))
perpendicular = float(input("Enter the perpendicular of the triangle: "))

triangle = Triangle(base, perpendicular)
hypotenuse = triangle.calculateHypotenuse()

print(f"The hypotenuse of the right angle triangle is: {hypotenuse}")


# In[ ]:




