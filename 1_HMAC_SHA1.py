# Example 1 (sha1):
import hmac

message = "Welcome to the repo"   # in case of dict, do json.dump(dict) or str(dict)
key= "aabbccddeeff"

# Method 1:
hmac1 = hmac.new(key=key.encode(), msg=message.encode(), digestmod="sha1")
message_digest1 = hmac1.digest()
print("{} - Message Digest 1 : {}".format(hmac1.name, message_digest1))

# Method 2:
hmac2 = hmac.new(key=key.encode(), digestmod="sha1")
hmac2.update(bytes(message, encoding="utf-8"))
message_digest2 = hmac2.digest()
print("{} - Message Digest 2 : {}".format(hmac2.name, message_digest2))

# Method 3:
hmac3 = hmac.new(key=key.encode(), digestmod="sha1")
hmac3.update(bytes("Welcome to ", encoding="utf-8"))
hmac3.update(bytes("the page.", encoding="utf-8"))
message_digest3 = hmac3.digest()     # in case of hexdigest, use .hexdigest()
print("{} - Message Digest 3 : {}".format(hmac3.name, message_digest3))

# The code at last prints digest size and block size for each HMAC instance.
print("Message Digest Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.digest_size, hmac2.digest_size,hmac3.digest_size,))
print("Message Block  Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.block_size, hmac2.block_size,hmac3.block_size,))
