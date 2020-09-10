#!/usr/bin/env python
# coding: utf-8

# # write a program to identify sublist [1,1,5] is there in the given list order,if yes print " its a match " else print " its gone" in function

# In[36]:


# to check if list is subset of other 
# using all() 
  
# initializing list 
test_list = [] 

# number of elements 
n = int(input("Enter number of elements : ")) 

for i in range(0, n): 
    ele = int(input()) 
    
    test_list.append(ele)
print(test_list) 

sub_list = [1,1,5] 
  
# printing original lists 
print ("Original list : " + str(test_list)) 
print ("Original sub list : " + str(sub_list)) 
  
# using all() to  
# check subset of list  
flag = 0
if(all(x in test_list for x in sub_list)): 
    flag = 1
      
# printing result 
if (flag) : 
    print ("Yes, list is subset of other.") 
else : 
    print ("No, list is not subset of other.") 


# # end
# 
