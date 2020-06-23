import sys
from hashlib import sha256
import json

def generateHash(platform, configFile = 'config.json'):
    with open(configFile) as f:
        data = json.load(f)
        secret = data["secret"]
        length = data["length"]
        if (length < 5 or length > 64):
            raise ValueError("Invalid length")

    raw = secret["str1"] + " " + str(sys.argv[1]) + " " + secret["str2"] + " " + str(length)
    hash = sha256(raw.encode('utf-8')).hexdigest()
    chopped = hash[:length]

    return chopped

def capitaliseAndSpecialChar(hash, specialChar = '!'):
    hash = list(hash)
    for i in range(len(hash)):
        c = hash[i]
        if c.islower():
            hash[i] = c.upper()
            break
    hash[-1] = specialChar
    return ''.join(hash)



n = len(sys.argv) 
if n != 2:
    raise ValueError("Invalid arguments")

hash = generateHash(sys.argv[1])
password = capitaliseAndSpecialChar(hash)
print(password)
