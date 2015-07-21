#!/usr/bin/python

print "Content-type: application/json"
print "Access-Control-Allow-Origin: *"
print ""

import cgi
import json
import os


def ensurePathForFile(filename):
    directory = os.path.dirname(filename)
    if not os.path.isdir(directory):
        # print "*Note* Folder '%s' doesn't exist. Creating for file '%s'" % (directory, filename)
        os.makedirs(directory)


def ensurePathForFolder(foldername):
    if not os.path.exists(foldername):
        # print "*Note* Folder '%s' doesn't exist. Creating now." % (foldername)
        os.makedirs(foldername)


def main():

    form = cgi.FieldStorage()

    username = form.getfirst("username", "")
    path = "save/%s/data.json" % (username)

    if os.path.isfile(path):
        data = json.loads(open(path).read())
    else:
        data = {}

    ret = json.dumps({
        "status": "OK",
        "data": data
    })

    print ret

if __name__ == "__main__":
    main()
