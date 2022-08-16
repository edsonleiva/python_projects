###### HIGH SCORE ######

# enter the scores seperated by spaces
from socket import socket

# enter the scores into the program
scores = input('Enter a list of scores: ').split()

# placeholder for high score
high_score = 0

# this loop converts score from str to int format
for x in range(0, len(scores)):
    scores[x] = int(scores[x])

print(scores)

# this loop checks the scores to see which score is the highest -- high score
for x in range(0, len(scores)):
    if x >= high_score:
        high_score = scores[x]
    else:
        continue

# print the high score
print(high_score)