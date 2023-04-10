# Introduction to HMAC

HMAC stands for Hash-based message authentication code

The HMAC is an algorithm that generates a hash of the message using a cryptographic hash  function  and a secret cryptographic key.

It can be used to check data for  integrity  and authenticity. It lets us calculate message authenticity and integrity using a shared key between two parties without the use of complex public key infrastructure involving certificates.

Python provides us with module name HMAC which provides an implementation for this algorithm. It takes as  input hashing algorithm name which is one of the algorithms which is available through *hashlib* library of Python.


# Methods

1. **new(key, message=None, digestmod=''):** This constructor creates an instance of HMAC with initial message given as bytes. It can be then used to generate message authentication code. We can only create an instance of HMAC as well without any initial message but we'll need key and digestmod. We can add messages using a call to update() method. The key needs to be in bytes format. The digestmod parameter accepts secure hashing algorithm names that are available through hashlib module.

2. **update(message_bytes):** This method adds messages given as input to already an existing message. We can call this method more than once and it'll keep on adding up messages.

3. **digest():** It returns the message authentication code of the data in bytes format. The size of the output is dependent on the input secure hashing algorithm. For example, if the input hashing algorithm is SHA1, then the output will be 20 bytes.

4. **hexdigest():** It returns message authentication code of data as hexadecimal digits. The hexadecimal digest will be twice the size of bytes digest because one byte can represent two hexadecimal digits. The size of the output is dependent on the input secure hashing algorithm. For example, if the input hashing algorithm is SHA1, then the output will be 40 hexadecimal digits.

# Attributes

1. **digest_size:** It returns an integer representing the number of bytes of secure hash that the algorithm will generate.

2. **block_size:** It returns an integer value representing the block size of the algorithm. The secure hash algorithms divide data into blocks where each block contains a number of bytes of data on which algorithm will work.



```python

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
hmac3.update(bytes("CoderzColumn.", encoding="utf-8"))
message_digest3 = hmac3.digest()     # in case of hexdigest, use .hexdigest()
print("{} - Message Digest 3 : {}".format(hmac3.name, message_digest3))

# The code at last prints digest size and block size for each HMAC instance.
print("Message Digest Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.digest_size, hmac2.digest_size,hmac3.digest_size,))
print("Message Block  Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.block_size, hmac2.block_size,hmac3.block_size,))

```
