#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Greet:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        return f"Hello, {self.first_name} {self.last_name}! Have a nice day!"

F = input("What is your first name? ")
L = input("What is your last name? ")


greet = Greet(F, L)
print(greet.greet())


# 
