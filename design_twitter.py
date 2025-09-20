from typing import List, DefaultDict
import heapq

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

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]: #go through all follwers
            if followeeId in self.tweetMap: #has at least one tweet so defined
                index = len(self.tweetMap[followeeId]) - 1 #the last one, most recent one
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId]) #need to keep track of followeeId cuz you have to keep decrementing this index, so have to keep it stored

        heapq.heapify(minHeap) #turn into heap, with valid head operations and stuff
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)       
