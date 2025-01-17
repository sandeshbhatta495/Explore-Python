class User:
    # Other methods remain the same...

    def view_feed(self):
        print(f"{self.name}'s Feed:")
        for user in self.following:
            for post in user.posts:
                print(f"{post.author.name}: {post.content} ({post.timestamp})")
