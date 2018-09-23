
# coding: utf-8

# In[3]:


#program that prints out a list of the integers from 1 to 20 and their squares.
print("Squares are : ")
for i in range(1,21):
    print(i,"-->",(i*i))


# In[4]:


#program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2
for i in range(100,1,-2):
    print(i,end=' ')


# In[5]:


import random
print(random.randint(3,6))


# In[6]:


import random
nums = [x for x in range(50)]
random.shuffle(nums)
print(nums)


# In[7]:


#Write a program that generates and prints 50 random integers, each between 3 and 6.
import random
for N in range(50):
    print(random.randint(3,6),end=' ')


# In[2]:


year=eval(input("Enter a year : "))
count=0
for i in range(1600,year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        count=count+1
print(count)

