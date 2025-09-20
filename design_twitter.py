class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None: