class Twitter:

    def __init__(self):
        self.user_follows = defaultdict(set)
        self.user_posts = defaultdict(list)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        self.user_follows[userId].add(userId)
        users_for_posts = list(self.user_follows[userId])
        for followee in users_for_posts:
            if not self.user_posts[followee]: continue
            max_heap.append((self.user_posts[followee][-1][0], len(self.user_posts[followee])-1, followee))

        heapq.heapify(max_heap)
        feed = []
        while max_heap and len(feed) < 10:
            _, i, followee = heapq.heappop(max_heap)
            feed.append(self.user_posts[followee][i][1])
            i -= 1
            if i == -1: continue
            heapq.heappush(max_heap, (self.user_posts[followee][i][0], i, followee))
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.user_follows[followerId]: return
        self.user_follows[followerId].remove(followeeId)
    
        
