#!/usr/bin/env python
# coding: utf-8

# In[2]:


class TypeChecker:
    def __init__(self, value):
        self.value = value
    
    def get_type(self):
        return type(self.value)


value = input("Enter a value: ")
checker = TypeChecker(value)
value_type = checker.get_type()

print(f"Input is: {value_type}")


# In[ ]:




