# Introduction to HMAC

HMAC stands for Hash-based message authentication code

The HMAC is an algorithm that generates a hash of the message using a cryptographic hash  function  and a secret cryptographic key.

It can be used to check data for  integrity  and authenticity. It lets us calculate message authenticity and integrity using a shared key between two parties without the use of complex public key infrastructure involving certificates.

Python provides us with module name HMAC which provides an implementation for this algorithm. It takes as  input hashing algorithm name which is one of the algorithms which is available through *hashlib* library of Python.


# Methods

1. **new(key, message=None, digestmod=''):** This constructor creates an instance of HMAC with initial message given as bytes. It can be then used to generate message authentication code. We can only create an instance of HMAC as well without any initial message but we'll need key and digestmod. We can add messages using a call to update() method. The key needs to be in bytes format. The digestmod parameter accepts secure hashing algorithm names that are available through hashlib module.

2. **update(message_bytes):** This method adds messages given as input to already an existing message. We can call this method more than once and it'll keep on adding up messages.

3. **digest():** It returns the message authentication code of the data in bytes format. The size of the output is dependent on the input secure hashing algorithm. For example, if the input hashing algorithm is SHA1, then the output will be 20 bytes.

4. **digest(key,msg,digest):** It accepts key, message to encode and digest algorithm as input and generates message authentication code for given input message.

5. **hexdigest():** It returns message authentication code of data as hexadecimal digits. The hexadecimal digest will be twice the size of bytes digest because one byte can represent two hexadecimal digits. The size of the output is dependent on the input secure hashing algorithm. For example, if the input hashing algorithm is SHA1, then the output will be 40 hexadecimal digits.

6. **compare(a,b):** This function compares two message authentication codes and returns True if they are equal else False. This function helps us prevent timing analysis attacks which can help attackers know the size of the message authentication code.

# Attributes

1. **digest_size:** It returns an integer representing the number of bytes of secure hash that the algorithm will generate.

2. **block_size:** It returns an integer value representing the block size of the algorithm. The secure hash algorithms divide data into blocks where each block contains a number of bytes of data on which algorithm will work.


# Example 1

```python

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


```

# Example 2

```python

# Example 2 (SHA256):
import hmac
import hashlib

message = "Welcome to the repo"   # in case of dict, do json.dump(dict) or str(dict)
key= "aabbccddeeff"

# Method 1:
hmac1 = hmac.new(key=key.encode(), msg=message.encode(), digestmod=hashlib.sha256)
message_digest1 = hmac1.digest()
print("{} - Message Digest 1 : {}".format(hmac1.name, message_digest1))

# Method 2:
hmac2 = hmac.new(key=key.encode(), digestmod=hashlib.sha256)
hmac2.update(bytes(message, encoding="utf-8"))
message_digest2 = hmac2.digest()
print("{} - Message Digest 2 : {}".format(hmac2.name, message_digest2))

# Method 3:
hmac3 = hmac.new(key=key.encode(), digestmod=hashlib.sha256)
hmac3.update(bytes("Welcome to ", encoding="utf-8"))
hmac3.update(bytes("the page.", encoding="utf-8"))
message_digest3 = hmac3.digest()
print("{} - Message Digest 3 : {}".format(hmac3.name, message_digest3))

# The code at last prints digest size and block size for each HMAC instance.
print("\nMessage Digest Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.digest_size, hmac2.digest_size,hmac3.digest_size,))
print("Message Block  Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.block_size, hmac2.block_size,hmac3.block_size,))

```

# Example 3
```Python
import hmac

message = "Welcome to the repo"   # in case of dict, do json.dump(dict) or str(dict)
key= "aabbccddeeff"

# Method 1:
hmac1 = hmac.new(key=key.encode(), msg=message.encode(), digestmod=hashlib.sha256)
message_digest1 = hmac1.hexdigest()
print("{} - Hex Message Digest 1 : {}".format(hmac1.name, message_digest1))

# Method 2:
hmac2 = hmac.new(key=key.encode(), digestmod=hashlib.sha256)
hmac2.update(bytes(message, encoding="utf-8"))
message_digest2 = hmac2.hexdigest()
print("{} - Hex Message Digest 2 : {}".format(hmac2.name, message_digest2))

# Method 3:
hmac3 = hmac.new(key=key.encode(), digestmod=hashlib.sha256)
hmac3.update(bytes("Welcome to ", encoding="utf-8"))
hmac3.update(bytes("the page.", encoding="utf-8"))
message_digest3 = hmac3.hexdigest()
print("{} - Hex Message Digest 3 : {}".format(hmac3.name, message_digest3))

# The code at last prints digest size and block size for each HMAC instance.
print("\nMessage Digest Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.digest_size, hmac2.digest_size,hmac3.digest_size,))
print("Message Block  Size for 1 : {}, 2 : {} and 3 : {}".format(hmac1.block_size, hmac2.block_size,hmac3.block_size,))
```

# Example 4 : SHA3_256 - digest
```python
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
```

# Example 5: compare() method
```Python
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
```


# Reference:
[https://the page.com/tutorials/python/hashlib-compute-secure-hashes-message-digests-in-python](https://coderzcolumn.com/tutorials/python/hashlib-compute-secure-hashes-message-digests-in-python)
