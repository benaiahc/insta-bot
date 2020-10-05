from InstagramAPI import InstagramAPI
from time import sleep

users_list = []
following_users = []


class InstaBot:

    def __init__(self):
        self.api = InstagramAPI("foodiedevotion", "Bcorious")

    def get_likes_list(self, username):
        api = self.api
        api.login()
        api.searchUsername(username)
        result = api.LastJson
        username_id = result['user']['pk']
        user_posts = api.getUserFeed(username_id)
        result = api.LastJson
        media_id = result['items'][0]['id']

        api.getMediaLikers(media_id)
        users = api.LastJson['users']
        for user in users:
            users_list.append({'pk': user['pk'], 'username': user['username']})
        bot.follow_users(users_list)

    def follow_users(self, users_list):
        api = self.api
        api.login()
        api.getSelfUsersFollowing()
        result = api.LastJson
        for user in result['users']:
            following_users.append(user['pk'])
        for user in users_list:
            if not user['pk'] in following_users:
                print('Following @' + user['username'])
                api.follow(user['pk'])
                sleep(120)
            else:
                print('Already following @' + user['username'])
                sleep(10)


bot = InstaBot()

bot.get_likes_list('foodytops')

