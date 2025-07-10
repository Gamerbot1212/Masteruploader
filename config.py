import os

class Config(object):
    BOT_TOKEN = os.environ.get("7818844996:AAFEy9ihAxPVKDTHanYvRb-gXEiOfUYxsCw")
    API_ID = int(os.environ.get("20831039"))
    API_HASH = os.environ.get("ea20b722f7af827db12fb85f4d55238c")
    AUTH_USER = os.environ.get('7597020624').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "PATEL BOY......"
