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
    title = form.getfirst("title", "")
    html = form.getfirst("html", "")

    folder = "pages/%s/" % (username)
    html_path = folder + "%s.html" % (title)

    ensurePathForFolder(folder)

    open(html_path, "w").write(html)

    ret = json.dumps({
        "status": "OK",
        "html_path": html_path
    })

    print ret

if __name__ == "__main__":
    main()
