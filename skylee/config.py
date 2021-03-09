class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1650661236:AAGx8FvurWpMWCuZLP4MCD6xpt54kDF1eZc"
    OWNER_ID = "645739169"
    OWNER_USERNAME = "Anomaliii"
    TELETHON_HASH = "ec3909aaa39889f44148d1f0e3c888be"
    TELETHON_ID = "1511741"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://vgsowlwmzikesa:a2721be0c59c5e47edd768a851a527c4b5fae8629f5a7b52ee0dd5dcc2f24018@ec2-54-145-102-149.compute-1.amazonaws.com:5432/db1192jtlqsn1c"  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = (
        []
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        []
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        []
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = None  # Your SpamWatch token
    WALL_API = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
