#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient, ASCENDING

client = MongoClient('localhost', 27017)
db = client.format

db.accountlogin.ensure_index('userid', unique=False)
print("accountlogin successfully ....")
db.accountlogout.ensure_index('userid', unique=False)
print("accountlogout successfully ....")
db.rolelogin.ensure_index('roleid', unique=False)
print("rolelogin successfully ....")
db.rolelogout.ensure_index('roleid', unique=False)
print("rolelogout successfully ....")
db.levelup.ensure_index('roleid', unique=False)
print("levelup successfully ....")


db.shoptrade.ensure_index([('roleid', ASCENDING), ('mallid', ASCENDING), ('itemid', ASCENDING)], unique=False)
print("shoptrade successfully ....")

db.addyuanbao.ensure_index([('roleid', ASCENDING), ('type', ASCENDING)], unique=False)
print("addyuanbao successfully ....")
db.costyuanbao.ensure_index([('roleid', ASCENDING), ('type', ASCENDING)], unique=False)
print("costyuanbao successfully ....")

db.starttask.ensure_index([('roleid', ASCENDING), ('taskid', ASCENDING)], unique=False)
print("starttask successfully ....")
db.endtask.ensure_index([('roleid', ASCENDING), ('taskid', ASCENDING)], unique=False)
print("endtask successfully ....")

db.gainitem.ensure_index([('roleid', ASCENDING), ('itemid', ASCENDING)], unique=False)
print("gainitem successfully ....")
db.loseitem.ensure_index([('roleid', ASCENDING), ('itemid', ASCENDING)], unique=False)
print("loseitem successfully ....")

