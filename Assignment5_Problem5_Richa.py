#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Factorial:
    def factorial(self, num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result


number = Factorial()

result_factorial = number.factorial(n)
print(f"The factorial of the number is: {result_factorial}")

