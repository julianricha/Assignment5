#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Square:
    def square_number(self, num):
        return num **2


operation = Square()

n1 = int(input("Input number to be squared: "))
result = operation.square_number(n1)

print(f"The square of the number is: {result}")


# In[ ]:




