import os
import pipes

def postBuild(site):
    cmd = 'lessc {static}/less/style.less {build}/static/css/style.css'
    cmd = cmd.format(build=pipes.quote(site.paths['build']),
                     static=pipes.quote(site.paths['static']))
    print 'Running less: {}'.format(cmd)
    os.system(cmd)
