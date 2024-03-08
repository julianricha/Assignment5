#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Calculator:
    def perform_operation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "Cannot divide by zero"
        else:
            return "Invalid operator"

n1 = int(input("Number 1 = "))
n2 = int(input("Number 2 = "))
o =  input("Operator (+ - * /) = ")


calc = Calculator()
result = calc.perform_operation(n1, n2, o)

print(f"{n1} {o} {n2} = {result}")


# In[ ]:




