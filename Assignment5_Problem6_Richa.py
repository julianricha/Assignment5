#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def display_counting(self):
        for number in range(self.start, self.end + 1):
            print(number)

start_number = int(input("Enter the start number: "))
end_number = int(input("Enter the end number: "))
counter = Counter(start_number, end_number)
counter.display_counting()


# In[ ]:




