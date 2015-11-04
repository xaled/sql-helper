__author__ = 'xaled'
import os
from mako.template import Template
from .filters import upperFirst

#TODO: make it oop!

helperTemplateFile = os.path.join(os.path.dirname(__file__),"templates/sqlite_jdbc/helper.java.tmp")
modelTemplateFile = os.path.join(os.path.dirname(__file__),"templates/sqlite_jdbc/model.java.tmp")


#-----------------
#Dictionaries

javatypes = {"string":"String", "int":"long", "bool":"boolean","float":"double","date":"long","blob":"byte[]"}
sqlitetypes = {"string":"TEXT", "int":"INTEGER", "bool":"INTEGER","float":"REAL","date":"INTEGER","blob":"BLOB"}


def checkConfig(config):
    print "checking Config..."
    return True

def createHelperClasses(config):
    checkConfig(config)
    # init vars
    db_name = config['database']
    db_version = config['database-version']
    err_profile = config['error-profile']
    classes = config['classes']
    rootpackage = "sqlhelper."+db_name.lower()
    if "root-package" in config:
        rootpackage = config['root-package']

    model_package = rootpackage+".model"
    model_dir = model_package.replace(".","/")
    helper_package = rootpackage+".dbhelper"
    helper_dir = helper_package.replace(".","/")

    classlist = list()
    # create model files
    for c in classes:
        classname = c['name']
        attributes = c['attributes']


        # privatevars
        vars = list()
        for a in attributes:
            type = a['type']
            jtype = javatypes[type]
            stype = sqlitetypes[type]
            varname = a['name']
            varnamelow = str(varname).lower()
            varname1up = varnamelow[0].upper() + varnamelow[1:]
            var= {"type":type, "jtype":jtype,"stype":stype, "name":varname,"namelow":varnamelow, "name1up":varname1up}
            vars.append(var)
        classlist.append({"name":c['name'],"vars":vars})

        modeldata = {"model_package":model_package, "dbname":db_name, "dbversion":db_version, "classname":classname,"vars":vars}
        modelTemplate = Template(filename=modelTemplateFile)
        class_text = modelTemplate.render(**modeldata)
        #print "class: ", classname, "\n"
        #print class_text
        os.system("mkdir -p '%s'"%(os.path.join("output",model_dir)))
        class_file = os.path.join("output",os.path.join(model_dir,classname+".java"))
        print "creating ", class_file
        fou = open(class_file,"w")
        fou.write(class_text)
        fou.close()


    # create helper file
    helperdata = {"dbname":db_name,"dbversion":db_version,"model_package":model_package, "helper_package":helper_package,"classes":classlist}
    helpertemplate = Template(filename=helperTemplateFile)
    helperclasstext = helpertemplate.render(**helperdata)
    #print "Helperclass: \n"
    #print helperclasstext
    os.system("mkdir -p '%s'"%(os.path.join("output",helper_dir)))
    helperclassname = upperFirst(db_name) + "DatabaseHandler"
    class_file = os.path.join("output",os.path.join(helper_dir,helperclassname+".java"))
    print "creating ", class_file
    fou = open(class_file,"w")
    fou.write(helperclasstext)
    fou.close()





