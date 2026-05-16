class Twitter:

    def __init__(self):
        self.user_follows = defaultdict(set)
        self.user_posts = defaultdict(set)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].add((-self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        self.user_follows[userId].add(userId)
        users_for_posts = list(self.user_follows[userId])
        for followee in users_for_posts:
            max_heap.extend(list(self.user_posts[followee]))
        heapq.heapify(max_heap)
        feed = []
        for _ in range(min(10, len(max_heap))):
            feed.append(heapq.heappop(max_heap)[1])
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.user_follows[followerId]: return
        self.user_follows[followerId].remove(followeeId)
        
