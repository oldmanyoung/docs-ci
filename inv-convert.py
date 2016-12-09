#!/usr/bin/python
import re
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-w",
        "--write",
        default = 'inventory.md',
        type = str,
        help = "File to write generated markdown")

    parser.add_argument(
        "-f",
        "--file",
        default = 'inventory',
        type = str,
        help = "Parse the contents of FILE into a markdown file")

    options = parser.parse_args()

    # pull in contents of inventory file as string
    rawhostsList = open(options.file).read()

    # strip off any extra newlines at end of file to make sure re.split
    # does not result in empty list element
    rawhostsList = rawhostsList.rstrip('\n')

    # cut out info from the new string
    hostsList = rawhostsList.replace('.cisco.com','')
    hostsList = hostsList.replace('ansible_ssh_port=','')
    hostsList = hostsList.replace('ansible_ssh_host=','')
    hostsList = hostsList.replace('ansible_user=','')
    hostsList = hostsList.replace('ansible_ssh_pass=','')

    # split the list of hosts into separate elements based on newline
    hostsList = re.split(r'\n', hostsList)

    # split list elements based on space delimiter
    hostsList = [ re.split(r' ', host) for host in hostsList ]

    # clean up leading/training spaces from list elements
    hostsList = [ map(str.strip, host) for host in hostsList ]


    #writefile = str(options.write)
    #print writefile
    with open(options.write,'w') as md:
        md.write("Generated from the inventory file in the [qaa-ansible-inventory](https://github.com/cisco-cis/qaa-ansible-inventory) repo\n")
        md.write("\n")
        md.write("Hostname | IP Address | SSH Port | SSH User | SSH Password \n")
        md.write("--- | --- | --- | --- | --- \n")

    for host in hostsList:
        with open(options.write,'a') as md:
                md.write(host[0] + " | " + host[1] + " | " + host[2] + " | " + host[3] + "| [see repo]\n")

if __name__ == "__main__" : main()
