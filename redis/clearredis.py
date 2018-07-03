#!/usr/bin/env python
# coding=utf-8

import sys
import getopt
import redis


def clear(userperfix):
    print("userperfix:{0}".format(userperfix))
    try:
        rc = redis.Redis(host='localhost', port=6380, db=0)
    except Exception, e:
        print("connect redis error ! \n {}".format(e))
        sys.exit()

    userkeys = rc.keys("{0}*".format(userperfix))
    #print userkeys
    for key in userkeys:
        print(">>>> del key: {0}".format(key))
        rc.delete(key)
    pass

def usage():
    print("python clearredis.py -u [username]")
    pass

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hu:")
    username=""
    for op, value in opts:
        if op == "-u":
            username = value
        elif op == "-h":
            usage()
            sys.exit()

    if username:
        clear(username)
    else:
        print("python clearredis.py -h")
