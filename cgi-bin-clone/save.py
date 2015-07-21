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
    # data_json = json.loads(form.getfirst("data", ""))
    data_txt = form.getfirst("data", "")

    folder = "save/%s/" % (username)
    txt_path = folder + "data.txt"
    # json_path = folder + "data.json"
    ensurePathForFolder(folder)

    # open(json_path, "w").write(json.dumps(data_json, indent=4))
    open(txt_path, "w").write(data_txt)

    ret = json.dumps({
        "status": "OK",
        # "json_path": json_path,
        "txt_path": txt_path
    })

    print ret

if __name__ == "__main__":
    main()
