#!/usr/bin/env python3

import os
import time
import subprocess

time.sleep(120)

start_time = time.time()

def check_running_time():
    current_time = time.time()
    elapsed_time = current_time - start_time
    return elapsed_time > 24 * 60 * 60

while True:
    if check_running_time():
        os.system('reboot now')

    if not os.path.exists('/dev/ttyACM0'):
        os.system('reboot now')
    result = subprocess.run(['docker', 'exec', '-i', 'otbr', 'ot-ctl', 'state'], capture_output=True)
    state = result.stdout.decode('utf-8').strip().split("\r\n")[0]
    print("Current otbr state: ", state)
    result = subprocess.run(['docker', 'exec', '-i', 'otbr', 'ot-ctl', 'dataset', 'active'], capture_output=True)
    dataset = "\n\t".join(result.stdout.decode('utf-8').strip().split("\r\n"))
    print("Current otbr dataset: \n", dataset)

    if not any(x in state for x in ["leader", "router"]):
        subprocess.run(['docker', 'compose', 'down'])
        subprocess.run(['docker', 'compose', 'up', '-d'])

    time.sleep(120)

