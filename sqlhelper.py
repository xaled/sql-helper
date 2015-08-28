__author__ = 'xaled'
import profiles
import os
import sys
import json


def Main(configFile):
    print "Importing config from ", configFile
    fin = open(sys.argv[1],"r")
    config = json.load(fin)
    fin.close()
    print "-"
    print json.dumps(config, indent=3)
    profiles.createHelperClasses(config)




if __name__ == "__main__":
    if len(sys.argv) <2:
        print "Need at least one argument: config file.\nSee example.json"
        sys.exit(1)
    Main(sys.argv[1])

