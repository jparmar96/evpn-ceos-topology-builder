#!/usr/bin/env python3
import os
import sys
import subprocess
from time import *

""" DISCLAIMER: This script starts 6 containers. Please run it on a server and not on your local machine."""



cmd = "docker import --change 'VOLUME /mnt/flash' cEOS-lab.tar.xz  ceosimage:latest"

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

cmd = ["docker create --name=ceos-leaf-1 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker",

"docker create --name=ceos-leaf-2 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker",

"docker create --name=ceos-leaf-3 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker",

"docker create --name=ceos-leaf-4 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker",

"docker create --name=ceos-spine-1 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker",

"docker create --name=ceos-spine-2 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker",
]
#docker create --name=ceos-host-1 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker

#docker create --name=ceos-host-3 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t ceosimage:latest /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

sleep(60)

cmd = ["docker network create nw1",
        "docker network create nw2",
        "docker network create nw3",
        "docker network create nw4",
        "docker network create nw5",
        "docker network create nw6",
        "docker network create nw7",
        "docker network create nw8"]
#docker network create nw9
#docker network create nw91

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

cmd = ["docker network connect nw1 ceos-leaf-1",
"docker network connect nw1 ceos-spine-1",
"docker network connect nw2 ceos-leaf-1",
"docker network connect nw2 ceos-spine-2",

"docker network connect nw3 ceos-leaf-2",
"docker network connect nw3 ceos-spine-1",
"docker network connect nw4 ceos-leaf-2",
"docker network connect nw4 ceos-spine-2",

"docker network connect nw5 ceos-leaf-3",
"docker network connect nw5 ceos-spine-1",
"docker network connect nw6 ceos-leaf-3",
"docker network connect nw6 ceos-spine-2",

"docker network connect nw7 ceos-leaf-4",
"docker network connect nw7 ceos-spine-1",
"docker network connect nw8 ceos-leaf-4",
"docker network connect nw8 ceos-spine-2"]

#docker network connect nw9 ceos-host-1
#docker network connect nw9 ceos-leaf-1
#docker network connect nw91 ceos-host-3
#docker network connect nw91 ceos-leaf-3

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

cmd = [
"docker start ceos-leaf-1",
"docker start ceos-leaf-2",
"docker start ceos-leaf-3",
"docker start ceos-leaf-4",
"docker start ceos-spine-1",
"docker start ceos-spine-2",
]
#docker start ceos-host-1
#docker start ceos-host-3
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

cmd = [
"docker cp ceos-leaf-1 ceos-leaf-1:/mnt/flash/ceos-leaf-1.cfg",
"docker cp ceos-leaf-2 ceos-leaf-1:/mnt/flash/ceos-leaf-2.cfg",
"docker cp ceos-leaf-3 ceos-leaf-1:/mnt/flash/ceos-leaf-3.cfg",
"docker cp ceos-leaf-4 ceos-leaf-1:/mnt/flash/ceos-leaf-4.cfg",
"docker cp ceos-spine-1 ceos-leaf-1:/mnt/flash/ceos-spine-1.cfg",
"docker cp ceos-spine-2 ceos-leaf-1:/mnt/flash/ceos-spine-2.cfg",
]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

sleep(30)

cmd = [
'docker exec ceos-leaf-1 Cli -p 15 -c "copy flash:ceos-leaf-1.cfg running-config"',
'docker exec ceos-leaf-1 Cli -p 15 -c "copy running-config startup-config"',
'docker exec ceos-leaf-2 Cli -p 15 -c "copy flash:ceos-leaf-1.cfg running-config"',
'docker exec ceos-leaf-2 Cli -p 15 -c "copy running-config startup-config"',
'docker exec ceos-leaf-3 Cli -p 15 -c "copy flash:ceos-leaf-1.cfg running-config"',
'docker exec ceos-leaf-3 Cli -p 15 -c "copy running-config startup-config"',
'docker exec ceos-leaf-4 Cli -p 15 -c "copy flash:ceos-leaf-1.cfg running-config"',
'docker exec ceos-leaf-4 Cli -p 15 -c "copy running-config startup-config"',
'docker exec ceos-spine-1 Cli -p 15 -c "copy flash:ceos-leaf-1.cfg running-config"',
'docker exec ceos-spine-1 Cli -p 15 -c "copy running-config startup-config"',
'docker exec ceos-spine-2 Cli -p 15 -c "copy flash:ceos-leaf-1.cfg running-config"',
'docker exec ceos-spine-2 Cli -p 15 -c "copy running-config startup-config"',
]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

sleep(30)

cmd = [
"docker stop ceos-leaf-1",
"docker start ceos-leaf-1",
"docker stop ceos-leaf-2",
"docker start ceos-leaf-2",
"docker stop ceos-leaf-3",
"docker start ceos-leaf-3",
"docker stop ceos-leaf-4",
"docker start ceos-leaf-4",
"docker stop ceos-spine-1",
"docker start ceos-spine-1",
"docker stop ceos-spine-2",
"docker start ceos-spine-2",
]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

sleep(60)
