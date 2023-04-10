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
