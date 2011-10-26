import cherrypy
from cherrypy.lib.static import serve_file
import json
import subprocess
import os

config = {
    "/css/basic.css" : {
        "tools.staticfile.on" : True
        ,"tools.staticfile.filename" : "/Users/sanctus/Programmation/html5/test1/css/basic.css"
        }
    
    }
class RunCommand(object):
    def app(self):
        file = open("app.html")
        data = file.read()
        file.close()
        return data
    app.exposed = True
    
    def ls(self):
        return json.dumps({ "type": 'file', "name" : "test.jpg" })
    ls.exposed = True


    def command(self, cmd):
        print("param : %s" % cmd)
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return json.dumps(result.stdout.read().split('\n'))
    command.exposed = True

cherrypy.quickstart(RunCommand(), config=config)
