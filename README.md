# sitediff
## Sitediff Readme 

###Prerequisite:

Make sure Ansible is installed and configured properly as sitediff.py will use Ansible Python API
(http://docs.ansible.com/ansible/developing_api.html)

###To Run :
1, switch to a environment, erither service cloud or tenant cloud

2, edit and review sitediff.yml, make sure there are no dangerous commands in chk_cmd

3, ./sitediff.py

###The Output:
--------------------Heading information-----------------------------------

Item1 : (cat /tmp/sitediff.pid/sometempfile for details.)

- Output1                             : Number of hosts having this output

- Output2                             : Number of hosts having this output

Item2 : (cat /tmp/sitediff.pid/sometempfile for details.)

- Output1                             : Number of hosts having this output

An Example Output:

--------------------Checking kernel on host group all-----------------------------------

kernel : (cat /tmp/sitediff.31035/tmpdje0SZ for details.)

- 3.10.0-229.4.2.el7.x86_64                                                        : 42

- 3.10.0-123.el7.x86_64                                                            : 1

--------------------Checking compute_packages on host group *-nova*---------------------

openstack-nova-compute : (cat /tmp/sitediff.31035/tmpsOvf0O for details.)

- openstack-nova-compute-2014.1.4-5.el7ost.noarch                                  : 36

openstack-nova-common : (cat /tmp/sitediff.31035/tmpbeZpOf for details.)

- openstack-nova-common-2014.1.4-5.el7ost.noarch                                   : 36
