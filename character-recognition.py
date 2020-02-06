# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:18:51 2019

@author: amuni
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:21:17 2019

@author: amuni
"""

import cv2
import numpy as np
import math 
import time

start_time = time.time()

image = cv2.imread("C:/transfer/Projects/CVIP_Summer/project1/data/proj1-task2.jpg", 0)
image1 = cv2.imread("C:/transfer/Projects/CVIP_Summer/project1/data/proj1-task2.jpg", 0)
templ1= cv2.imread("C:/transfer/Projects/CVIP_Summer/project1/data/c.png", 0)
#templ2=  cv2.imread("C:/transfer/Projects/CVIP_Summer/project1/data/a.jpg", 0)
#print(templat)
#maxm = np.max(image)
#minm = np.min(image)
#image = (image-minm)/(maxm -minm) 
#maxm1 = np.max(templ)
#minm1 = np.min(templ)
#templ = (templ-minm1)/(maxm1 -minm1)
#cv2.imwrite('imagever.jpg',image) 
#blur = cv2.GaussianBlur(image,(3,3),0)
#templ = cv2.GaussianBlur(templ,(3,3),0)
#image=cv2.Laplacian(blur,cv2.CV_32F,3)
#templ=cv2.Laplacian(templ,cv2.CV_32F,3)

length = templ1.shape[0]
if length % 2 == 0:
    bl = length/2 
else:
     bl = (length+1)/2   
bl = math.floor(bl)
breadth = templ1.shape[1]
if breadth % 2  == 0:
    bc = breadth/2 
else:
     bc = (breadth+1)/2 
bc = math.floor(bc)
rows  = image.shape[0]
columns = image.shape[1]
#print(length)

elapsed_time = time.time() - start_time

print(elapsed_time)

#match_pos = [[0 for a in range(columns)] for b in range(rows)]
match_pos1 = np.zeros((rows, columns))
match_pos2 = np.zeros((rows, columns))
for i in range(rows-length+1):
    for j in range(columns-breadth+1):
        for tx in range(length):
            for ty in range(breadth):
                
                #match_pos[i,j] += np.abs((image[i+tx, j+ty] - templ[tx, ty])) 
                match_pos1[i,j] += np.square(image[i+tx, j+ty] - templ1[tx, ty])
                ##if match_pos[i,j] == 0:
                ###match_pos2[i,j] += np.square(image[i+tx, j+ty] - templ2[tx, ty])    
        #match_pos[i, j] = np.sqrt(match_pos[i, j])
                    ##print(match_pos[i, j])
'''
#for i in range(rows-length+1):
#    for j in range(columns-breadth+1):
#       match_pos[i,j] =   
'''        
elapsed_time = time.time() - start_time

print(elapsed_time)

print("breakpoint1")        
#match_pos = np.asarray(match_pos)
w, h = templ1.shape[::-1]
loc1 = np.where(match_pos1 <= 4000) 
#loc2 = np.where(match_pos2 <= 4500 )
print(match_pos1[i,j])
#print (loc)

for pt in zip(*loc1[::-1]):
    cv2.rectangle(image1, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)             
'''
for pt in zip(*loc2[::-1]):
    cv2.rectangle(image1, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
'''
cv2.imwrite('matchedc1.jpg',image1)                
#print(match_pos[6,7])