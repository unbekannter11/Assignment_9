#!/usr/bin/env python
# coding: utf-8

# In[ ]:


password = "W@12\"\,"
name = "Joseph"
enter_name = input("Enter your first name please : ")

if name == enter_name :
    output = f"Hello, Joseph! The password is {password} ."
elif name != enter_name :
    output = "Hello Amina! See you later."
print(output)

