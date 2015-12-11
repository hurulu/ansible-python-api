#!/usr/bin/env python

import ansible.runner
import yaml
import tempfile
import os
import sys

def read_conf(conf_file):
    with open(conf_file, 'r') as ymlfile:
        return yaml.load(ymlfile)

def ansible_run(chk_item,chk_cmd,chk_hosts):
    runner = ansible.runner.Runner(
       module_name='shell',
       module_args=chk_cmd,
       pattern=chk_hosts,
       forks=10
    )
    datastructure = runner.run()
    versions = {}
    for i in  datastructure['contacted'].items():
        ver = i[1]['stdout']
        host = i[0]
        if ver in versions:
            versions[ver].append(host)
        else:
            versions[ver] = []
            versions[ver].append(host)
    return versions
def ansible_host_count(chk_hosts):
    runner = ansible.runner.Runner(
       module_name='shell',
       module_args='ansible ' + chk_hosts + ' --list-hosts|wc -l',
       pattern=chk_hosts,
       forks=10
    )
    datastructure = runner.run()
    return len(datastructure['contacted'])

def show_result(result):
    for key in result:
        print "- %-80s : %d" % (key, len(result[key]))

def write_details(result):
    tempdir = '/tmp/sitediff.' + str(os.getpid())
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
    temp = tempfile.NamedTemporaryFile(dir=tempdir, delete=False)
    try:
    	temp.write(yaml.safe_dump(result,default_flow_style=False))
    finally:
        temp.close()
        return temp.name

if __name__ == '__main__':
    conf = __file__.replace(".py",".yml")
    if not os.path.isfile(conf):
        print "ERROR : %s is not found." % conf
        sys.exit(1)
    cfg = read_conf(conf)
    for item in cfg:
        chk_hosts = cfg[item]['hosts']
	#host_count = ansible_host_count(chk_hosts)
        chk_cmd = cfg[item]['chk_cmd']
        heading = '-' * 20 + 'Checking ' + item + ' on host group ' + chk_hosts + '-' * 60
        print heading [0:88]
	if 'list' in cfg[item]:
            for i in cfg[item]['list']:
		chk_result = {}
                chk_cmd = cfg[item]['chk_cmd'] + " " + i
		chk_result = ansible_run(i,chk_cmd,chk_hosts)
                details_file = write_details(chk_result)
                print "%s : (cat %s for details.)" % (i, details_file)
        	show_result(chk_result)
	else:
	    chk_result = {}
            chk_result = ansible_run(item,chk_cmd,chk_hosts)
            details_file = write_details(chk_result)
            print "%s : (cat %s for details.)" % (item, details_file)
            show_result(chk_result)
