#!/usr/bin/env python2
import subprocess,re,json

process = subprocess.Popen(["vtysh", "-c", "show ip bgp summary"], stdout=subprocess.PIPE)
out, err = process.communicate()
peers = re.findall( r'[0-9]+(?:\.[0-9]+){3}', out)
out = {"data": []}
for peer in peers:
    out["data"].append({ "{#BGPPEER}": peer}) 
print(json.dumps(out, indent=4, sort_keys=True))
