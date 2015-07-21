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
    txt_path = "save/%s/data.txt" % (username)
    json_path = "save/%s/data.json" % (username)

    data_json = {}
    data_txt = ""

    if os.path.isfile(json_path):
        data_json = json.loads(open(json_path).read())

    if os.path.isfile(txt_path):
        data_txt = open(txt_path).read()

    ret = json.dumps({
        "status": "OK",
        "data_json": data_json,
        "data": data_txt
    })

    print ret

if __name__ == "__main__":
    main()
