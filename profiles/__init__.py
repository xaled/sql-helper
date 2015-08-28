__author__ = 'xaled'


def createHelperClasses(config):
    profile = "default"
    try:
        profile = config['output-profile']
    except:
        import sys
        print "Unexpected error:", sys.exc_info()[0]
    if profile == "default" or profile=="sqlite_jdbc":
        from . import sqlite_jdbc
        sqlite_jdbc.createHelperClasses(config)
    else:
        print "Couldn' find profile: %s."%(profile)
