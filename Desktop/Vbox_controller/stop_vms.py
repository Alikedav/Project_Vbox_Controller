#!/usr/bin/env python
import argparse
import re
import os
import subprocess

try:
    import json
except ImportError:
    import simplejson as json



def poweroff_vm(vm_id):
    """
    Issues a 'poweroff' command to VirtualBox for the given VM.
    """
    print ("Powering off VM: %s..." % vm_id)
    output = subprocess.Popen(['VBoxManage', 'controlvm', vm_id, 'poweroff'])

results = poweroff_vm(vm_id)
print(results)
