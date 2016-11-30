#!/usr/bin/python

import argparse
import requests
import json
import sys

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f",
        "--file",
        default = None,
        type = str,
        help = "Write the contents of FILE to the confluence page")

    parser.add_argument(
        "html",
        type = str,
        default = None,
        nargs = '?',
        help = "Write the immediate html string to confluence page")

    options = parser.parse_args()

    if options.html is not None and options.file is not None:
        raise RuntimeError(
            "Can't specify both a file and immediate html to write to page!")

    if options.html:
        html = options.html

    else:
        with open(options.file, 'r') as fd:
            html = fd.read()

#    file = open('test.md', 'r')
#    filestring = file.read()

    giturl = "https://api.github.com/markdown"
    payload = {'text': html}

    r = requests.post(giturl, data=json.dumps(payload))
    #print(r.text)
    temphtml = r.text
#    print(temphtml)
    f = open('tempfile.html', 'w')
    f.write(temphtml)
    f.close()

if __name__ == "__main__" : main()
