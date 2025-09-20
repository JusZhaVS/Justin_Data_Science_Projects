class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) #to store userIds and corresponding followeeIds
        self.tweetMap = defaultdict(list) = #store userIds and tweets as a min heap of (count, tweetId)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        if len(self.tweetMap[userId] > 10):
            self.tweetMap[userId].pop(0) #pop from the front so popping the oldest element, inefficient but wtv
        self.time -= 1 #dec cuz min heap, so want newer elements to the front 

#    def getNewsFeed(self, userId: int) -> List[int]:
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)       
