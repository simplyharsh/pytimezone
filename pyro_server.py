#!/usr/bin/python
from __future__ import print_function

import Pyro4
from api import pytimezone
pyt = pytimezone()

daemon=Pyro4.Daemon()
uri=daemon.register(pyt)

f = open("tzlatlng_obj_uri",'w')
print(uri, file=f)
f.close()

print("Ready. Object uri =", uri)

daemon.requestLoop()
