from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.input_path = 'content'
env.deploy_path = 'output'

def build():
    local('pelican {input_path} -o {deploy_path} -s pelicanconf.py'.format(**env))

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def gh_pages():
    local('cd {deploy_path} && '
            'pwd && '
            'git st && '
            'git add --all . && '
            'git ci -am "re-build from local by markdoc @MBP111216ZQ" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'date '.format(**env)
          )

def pub():
    build()
    #CNAME()
    gh_pages()

'''
#DEPLOY_PATH = env.deploy_path
env.qiniu = '/opt/bin/7niu_package_darwin_amd64/qrsync'
env.qiniu_conf = '../../7niu4pychina.json'
#env.qiniu_path = '../7niu.pyconcn'

def pub2hub():
    build()
    local('cd {deploy_path} && '
            'git status && '
            'git add . && '
            'git commit -am \'upgraded from local. by StaticPyCon\' && '
            'git push origin gitcafe-pages'.format(**env)
          )

def put7niu():
    build()
    local('cd {deploy_path} && '
            'pwd && '
            '{qiniu} {qiniu_conf}&& '
            'date '.format(**env)
          )

'''

