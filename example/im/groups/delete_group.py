from im import users
from im import common
from conf import *
import time

import json
jmessage=common.JMessage(app_key,master_secret)

groups=jmessage.create_groups()

response=groups.delete_group("10184263")
time.sleep(2)
print response