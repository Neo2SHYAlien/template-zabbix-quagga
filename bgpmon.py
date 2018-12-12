#!/usr/bin/env python2
import subprocess,re,sys

arg = sys.argv[1]
if arg:
  process = subprocess.Popen(["vtysh", "-c", "show ip bgp summary"], stdout=subprocess.PIPE)
  out, err = process.communicate()
  for line in out.split("\n"):
    if arg in line:
      end = line.strip()[-1]
      if end.isdigit():
        print 1
        exit(0)
  print 0
