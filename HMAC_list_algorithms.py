# Below we have printed names of the algorithms available through hashlib library. 

import hashlib

print("List of Available Algorithms to Construct Secure Hash/Message Digest : {}"
      .format(hashlib.algorithms_available))

print("List of Algorithms Guaranteed to Work : {}"
      .format(hashlib.algorithms_guaranteed))

print("List of Algorithms that May Work : {}"
      .format(hashlib.algorithms_available.difference(hashlib.algorithms_guaranteed)))