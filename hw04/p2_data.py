"""
Start file for hw1pr2 of Big Data Summer 2017

This file is used to load and process data for problem 2, and is imported

Note:
1. Please DO NOT change anything in this file.
2. Although these codes are given, please read carefully through the file, and
   make sure you understand how these codes work.
"""
import pandas as pd
import numpy as np

from os import path


print('==>Loading data...')

# create the headers for data frame since original data dodes not have headers
name_list = ['pix_{}'.format(i + 1) for i in range(784)]
name_list = ['label'] + name_list

if path.exists("df_train.pkl"):
	df_train = pd.read_pickle("df_train.pkl")
else:
	df_train = pd.read_csv('http://pjreddie.com/media/files/mnist_train.csv', \
		sep=',', engine='python', names = name_list)
	df_train.to_pickle("df_train.pkl")

if path.exists("df_test.pkl"):
	df_test = pd.read_pickle("df_test.pkl")
else:
	df_test = pd.read_csv('http://pjreddie.com/media/files/mnist_test.csv', \
		sep=',', engine='python', names = name_list)
	df_test.to_pickle("df_test.pkl")

print('==>Data loaded succesfully.')


# Process training data, so that X (pixels) and y (labels) are seperated
X_train = np.array(df_train[:][[col for col in df_train.columns \
	if col != 'label']]) / 256.

y_train = np.array(df_train[:][['label']])


# Process test data, so that X (pixels) and y (labels) are seperated
X_test = np.array(df_test[:][[col for col in df_test.columns \
	if col != 'label']]) / 256.

y_test = np.array(df_test[:][['label']])
