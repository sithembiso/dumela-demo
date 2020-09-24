import hashlib

# Admin login
username = 'admin'
password = 'P@ssw0rd'

# System settings. More changes on this file
secret = hashlib.md5()
# m.update("L3P5+4-{}".format(date.today()).encode('utf-8'))