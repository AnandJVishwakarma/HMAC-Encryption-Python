# Example 4 (SHA3_256 - digest):
# We can digest() method to generate message authentication code for the given message using input key directly without creating an instance of HMAC instance. This method works fast compared to creating authentication code for small messages through HMAC instance because it uses optimized C implementation for creating digest.

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
