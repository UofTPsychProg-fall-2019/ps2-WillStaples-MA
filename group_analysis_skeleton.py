#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
  
#for loop to read in data - can't figure it out so I read in the data manually
#Below in my attempt at the for loop
testingrooms = ['A','B','C']
data = np.empty((0,5))
for room in testingrooms:
    filename = 'datafile'+room+'.csv'
    print(filename)
    tmp = sp.loadtxt('',delimiter=',')
    data = np.vstack([data,tmp])

#Below is how I actually read in the data
testingroomA = sp.loadtxt('C:/Users/Will Staples/Desktop/Will-Staples/ps2-WillStaples-MA/rawdata/experiment_data_A.csv', delimiter=',')

testingroomB = sp.loadtxt('C:/Users/Will Staples/Desktop/Will-Staples/ps2-WillStaples-MA/rawdata/experiment_data_B.csv', delimiter=',')

testingroomC = sp.loadtxt('C:/Users/Will Staples/Desktop/Will-Staples/ps2-WillStaples-MA/rawdata/experiment_data_C.csv', delimiter=',')

a = np.concatenate((testingroomA, testingroomB, testingroomC), axis=0)
a.astype(int)


#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#
data = np.empty((0,5))
for room in testingrooms:
...


#%%
# calculate overall average accuracy and average median RT

#average accuracy using numpy mean function and slicing
np.mean(a[0:,3:4])
Out[27]: 0.9147865812499999

#average median RT using numpy mean function and slicing
np.mean(a[0:,4:5])
Out[28]: 477.3369565217391
  
acc_avg = ...   # 91.48%
mrt_avg = ...   # 477.3ms


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#
#for loop & if/else statements to determine condition means
word_acc=0

word_mrt=0

word_count=0

face_acc=0

face-mrt=0

face_mrt=0


for x in range(92): #variable explorer indicates there are 92 rows
    if a[x,1]==2: #faces
        face_acc = face_acc+a[x,3] # add accuracy score to face accuracy variable
        face_mrt = face_mrt+a[x,4] # add mrt score to face mrt variable
        face_count = face_count+1 # add one to the face count
    else:
        word_acc=word_acc+a[x,3]# add accuracy score to word accuracy variable
        word_count=word_count+1 #add one to the word count
        woed_mrt=word_mrt+a[x,4] #add mrt score to word mrt variable
        
face_acc_mean=face_acc/face_count
face_acc_mean
Out[66]: 0.944009886369565

face_mrt_mean=face_mrt/face_count
face_mrt_mean
Out[68]: 465.30434782608694

word_acc_mean=word_acc/word_count
word_acc_mean
Out[70]: 0.8872829203617021

word_mrt_mean=word_mrt/word_count
word_mrt_mean
Out[80]: 478.9574468085106

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms


#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
acc_wp = ...  # 94.0%
acc_bp = ...  # 88.9%
mrt_wp = ...  # 469.6ms
mrt_bp = ...  # 485.1ms


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)

#averages using sliing, indexing, and np.mean function
acc_wp = np.mean(a[a[...,2]==1],axis=0)[3]# .94
acc_bp = np.mean(a[a[...,2]==2],axis=0)[3]# 88.9
mrt_wp = np.mean(a[a[...,2]==1],axis=0)[4]# 469.6
mrt_bp = np.mean(a[a[...,2]==2],axis=0)[4]# 485.1

# words - white/pleasant: 478.4ms
# words - black/pleasant: 500.3ms
# faces - white/pleasant: 460.8ms
# faces - black/pleasant: 469.9ms


#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats
#make 2 data sets for word and face data
face_data=[]

word_data=[]


#append the corresponding rows
for x in range(92): 
    if a[x,1]==2:
        face_data.append(a[x:])
    else:
        word_data.append(a[x:])
        
        #this approach did not work

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...

