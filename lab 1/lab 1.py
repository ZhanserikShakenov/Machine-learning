#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy
import re


# In[13]:


with open("C:\\Users\\aka-studio\\Desktop\\Assignments\\ML\\sentences.txt", 'r') as f:
    sentences = f.read()
arr = sentences.lower().split('\n')
arr_f = arr
arr


# In[14]:


for i in range(len(arr)):                               
    arr[i] = re.split('[^a-z]', arr[i])    
    for j in range(arr[i].count('')):        
        arr[i].remove('')
arr


# In[15]:


unique = list(set([word for arr_f in arr for word in arr_f]))
d={}
cnt = 0
for i in unique:                       
    d[i] = cnt
    cnt +=1
d


# In[19]:


matrix = numpy.zeros((len(arr_f), len(unique)))
matrix.shape
for i, j in enumerate(arr):
    for z in j:
        matrix[i, d[z]] = j.count(z)
matrix


# In[17]:


def cos_distance(x, y):
    return 1 - x@y/(numpy.sqrt(x@x)*numpy.sqrt(y@y))
distances=numpy.array([cos_distance(matrix[0],matrix[i]) for i in range(1, matrix.shape[0])])
distances


# In[18]:


numpy.argsort(distances)[:2] + 1

