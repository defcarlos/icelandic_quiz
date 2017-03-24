#!/usr/bin/env python3
# coding=utf-8

import json
import random
import string

with open('icelandic.json', 'r') as fp:
    data = json.load(fp)

#also need to think about how to keep from getting the same question again if answered correctly. My guess right now
#is something similar to pop for dictionaries
#last improvement i can think of is to allow for the user to select a dictionary to use. i.e. lession1, lession2
#I would then load what was selected dynamically.

correct = 0
wrong = 0

'''Notes: Below is a simple for loop that implements the quiz.
The for loop iterates through the keys in the dictionary and uses them in the input to the user.
The user input is stored in a variable and then made lowercase to match against the values in the dictionary.
The rest steps through to give the user feedback regarding the correctness of his/her answer and gives them
the number of items they have answered correctly as well as the number answered incorrectly.
The user also receives some feedback when incorrect and is told what the answer should be.
This could be made more robust by using NLP so that the user could enter an answer that gets at the meaning
of the word or phrase without saying the exact translation stored.'''
print('Instrictions: To end the quiz type the word break.')
for k in data.keys():
	response = input('what does ' + k + ' mean?: ')
	response = response.lower()
	if response == data[k]:
		correct = correct + 1
		print('correct!')
		print('answered correctly: ', correct)
		print('answered incorrectly: ',wrong)
	elif response == 'break':
		print('thanks for taking the quiz')
		print('answered correctly: ', correct)
		print('answered incorrectly: ',wrong)
		break
	else:
		wrong = wrong + 1
		print('incorrect. the answer is: ' + data[k])
		print('answered correctly: ', correct)
		print('answered incorrectly: ',wrong)
  
		