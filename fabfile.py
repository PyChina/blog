from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.input_path = 'content'
env.deploy_path = 'output'
#DEPLOY_PATH = env.deploy_path
env.qiniu = '/opt/bin/7niu_package_darwin_amd64/qrsync'
env.qiniu_conf = '../../7niu4pychina.json'
#env.qiniu_path = '../7niu.pyconcn'

def put7niu():
    build()
    local('cd {deploy_path} && '
            'pwd && '
            '{qiniu} {qiniu_conf}&& '
            'date '.format(**env)
          )

def build():
    local('pelican {input_path} -o {deploy_path} -s pelicanconf.py'.format(**env))

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()
