# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('23830477'))
    API_HASH = str(getenv('19f8365d98fb11c9cd6c1eaa8b1fa4b8'))
    BOT_TOKEN = str(getenv('6074196500:AAEJIO57QOP1_Aig2i9poQ4XRMcE9tLsy4A'))
    name = str(getenv('name', 'renamer1111bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('-1001871138407'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1867884587").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME'))
    OWNER_USERNAME = str(getenv('SpidyRockss'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('renamer1111bot'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
