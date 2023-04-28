#!/usr/bin/env python
# coding: utf-8

# In[1]:


def triple_numbers(nums):
    tripled_nums = map(lambda x: x * 3, nums)
    return list(tripled_nums)
my_list = [1, 2, 3, 4, 5, 6, 7]
result = triple_numbers(my_list)
print(result) 


# In[ ]:




