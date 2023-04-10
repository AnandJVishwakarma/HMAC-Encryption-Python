# Example 5:
# We are explaining how we can use compare() method of hmac module to compare message authentication codes.

import hmac
import hashlib

message = "Welcome to the repo"   # in case of dict, do json.dump(dict) or str(dict)
key= "aabbccddeeff"

# Method 1:
message_digest1 = hmac.digest(key=key.encode(), msg=message.encode(), digest="sha3_256")
print("Message Digest 1 : {}".format(message_digest1))

# Method 1:
message_digest2 = hmac.digest(key=key.encode(), msg=bytes(message, encoding="utf-8"), digest=hashlib.sha3_256)
print("Message Digest 2 : {}".format(message_digest2))
print("Is message digest 1 is equal to message digest 2? : {}".format(hmac.compare_digest(message_digest1, message_digest2)))
