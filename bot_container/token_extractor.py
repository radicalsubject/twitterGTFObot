import os
try: 
    f = open("token.secret", "r")
    token = f.read()
except:
    token = os.environ("BOT_TOKEN")