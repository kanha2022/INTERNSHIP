#!/usr/bin/env python
# coding: utf-8

# In[62]:


#Q11 to Q15 are programming questions. Answer them in Jupyter Notebook.



# In[51]:


#11. Write a python program to find the factorial of a number.
# factorial of given number
def factorial(n):
    if n==0:
        result=1
    else:
        result= n*factorial(n-1)
    return result
print("factorial of given no. is:",factorial(6))   


# In[ ]:


12. Write a python program to find whether a number is prime or composite.

num = 11
  
# If given number is greater than 1
if num > 1:
  
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
  
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")


# In[ ]:





# In[19]:


#13. Write a python program to check whether a given string is palindrome or not.

# function return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
 

s = "level"
a = isPalindrome(s)
 
if a :
    print("Yes")
else:
    print("No")


# In[56]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.

def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if a == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return 
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[61]:


#15. Write a python program to print the frequency of each of the characters present in a given string.
# initializing string 
a = "happyvibes"
  
 # frequency of each of the characters present in a given string 
freq = {}
  
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
  

print ("Count of all characters in happyworld is :\n " +  str(freq))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




