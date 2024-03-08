#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Calculator:
    def add(self, num1, num2):
        return num1 + num2

def main():
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    calc = Calculator()
    print("The sum is:", calc.add(num1, num2))

main()


# In[ ]:




