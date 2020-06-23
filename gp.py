import argparse
from hashlib import sha256
import getpass 
import random

def generateHash(platform, secretString, length):
    raw = list(secretString + ' ' + str(platform).lower() + ' ' + str(length))
    random.Random(length).shuffle(raw)
    shuffled = ''.join(raw)
    
    hashed = sha256(shuffled.encode('utf-8')).hexdigest()
    chopped = hashed[:length]
    return chopped

def capitaliseAndSpecialChar(hashed, specialChar = '!'):
    hashed = list(hashed)
    hashed[-1] = specialChar
    
    for i in range(len(hashed)):
        c = hashed[i]
        if c.islower():
            hashed[i] = c.upper()
            break
    
    return ''.join(hashed)

def getPassword(platform, secretString, length):
    hashed = generateHash(platform, secretString, length)
    password = capitaliseAndSpecialChar(hashed)
    return password

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Generate Password: Personal multi-platform password generation scheme')
    parser.add_argument('platform', type=str, help='name of platform for which password should be generated', nargs='?', metavar='PLATFORM')
    parser.add_argument('--list', type=str, help='path to file containing all platforms', metavar='PATH')
    parser.add_argument('--length', type=int, help='required length of generated password', metavar='LENGTH')
    args = parser.parse_args()

    if args.platform == None and args.list == None:
        raise ValueError('Invalid usage. Use --help for more information.')
    elif args.platform != None and args.list != None:
        raise ValueError('Invalid usage. Use --help for more information.')
    elif args.platform == '' or args.list == '':
        raise ValueError('Invalid usage. Use --help for more information.')
    
    length = 16 if args.length == None else args.length
    if length < 5 or length > 64:
        raise ValueError('Invalid length')
    
    
    if args.list == None:
        secretString = getpass.getpass(prompt='Enter your secret string: ')
        print()

        platform = args.platform.lower()
        password = getPassword(platform, secretString, length)
        print ("{:<20} {:<64}".format(platform + ':', password))
    else: 
        with open(args.list) as f:
            platforms = f.readlines()
            platforms = [platform.rstrip().lower() for platform in platforms]
            platforms = [platform for platform in platforms if platform]
        
        secretString = getpass.getpass(prompt='Enter your secret string: ')
        print()

        for platform in platforms:
            password = getPassword(platform, secretString, length)
            print ("{:<20} {:<64}".format(platform + ':', password)) 