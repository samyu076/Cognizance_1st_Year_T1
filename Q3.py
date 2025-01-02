import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    # Write your code here
    scores = sorted(set(ranked), reverse=True)  
    result = []  
    i = len(scores)
    for score in player:
          while i > 0 and score >= scores[i - 1]:
            i -= 1 
          result.append(i + 1)
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
