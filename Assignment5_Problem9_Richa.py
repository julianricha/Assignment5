#!/usr/bin/env python
# coding: utf-8

# In[1]:


class PowerCalculator:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent
    
    def calculate_power(self):
        return self.base ** self.exponent


base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

calculator = PowerCalculator(base, exponent)
result = calculator.calculate_power()
    
print(f"{base} to the power {exponent} = {result}")


# In[ ]:




