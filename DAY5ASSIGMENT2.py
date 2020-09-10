#!/usr/bin/env python
# coding: utf-8

# # filtering prime numbers between 1 to 2500
# 

# In[1]:


def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(1,2500))
print ('Prime numbers between 1-10:', list(fltrObj))


# # end
