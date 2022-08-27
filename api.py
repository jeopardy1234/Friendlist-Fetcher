from time import time
import requests
from hashlib import sha512

key = "YOUR-KEY"
secret = "YOUR-SECRET"
rnd = "237514"
method = "user.friends"
tme = int(time())
hashStr = f"{rnd}/{method}?apiKey={key}&onlyOnline=false&time={tme}#{secret}"
hash = sha512(hashStr.encode('utf-8')).hexdigest()
url = f"https://codeforces.com/api/{method}?apiKey={key}&onlyOnline=false&time={tme}&apiSig={rnd}{hash}"

r = requests.get(url)
#send data to json file
with open('friends.json', 'w') as f:
    f.write(r.text)