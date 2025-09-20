from typing import List, DefaultDict
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # userId -> llist of [count, tweetIds]
        self.tweetMap = defaultdict(list) # userId -> set of followeeId
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        if len(self.tweetMap[userId] > 10):
            self.tweetMap[userId].pop(0) #pop from the front so popping the oldest element, inefficient but wtv
        self.time -= 1 #dec cuz min heap, so want newer elements to the front 



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)       
