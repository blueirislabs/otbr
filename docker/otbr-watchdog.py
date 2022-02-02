#!/usr/bin/env python3

import subprocess
from subprocess import PIPE

result = subprocess.run(['ot-ctl', 'state'], stdout=PIPE, stderr=PIPE)
state = result.stdout.decode('utf-8').strip().split("\r\n")[0]
print("Current otbr state: ", state)
result = subprocess.run(['ot-ctl', 'dataset', 'active'], stdout=PIPE, stderr=PIPE)
dataset = "\n\t".join(result.stdout.decode('utf-8').strip().split("\r\n"))
print("Current otbr dataset: \n", dataset)

if not any(x in state for x in ["leader", "router"]):
    exit(1)
exit(0)
