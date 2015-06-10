RSA Cryptography implementation in Python

This is a basic Python code to implement RSA Cryptography. The aim was to learn to code in Python and to learn about RSA Cryptosystem. 
Firstly, Prime numbers are genereted using primegeneration.py. The generated data is then inserted wherever necessary in the 
encryption.py and decryption.py files. The prime numbers generated are not huge though they are each around 8 digits long. 
But for an illustration this serves the purpose.. 
The prime number generation can be made faster using Rabin-Miller Primality testing.

The encryption.py file is to be run next. Before that one has to paste the public key and the modulus from the primegeneration.py 
execution. The text to be encrypted is input. At present only alphabets, digits and spaces are supported. One can modify that. 
Then padding is done to further show how it is done in the real world. Then the message is encrypted and converted to hexadecimal 
text. The output is a hexadecimal stream of characters.

Then one has to provide this stream of characters as input for the decryption.py file. But firstly one has to copy the values of 
private key, modulus, prime numbers p and q from primegeneration.py to decryption.py. Then after providing the input, the stream 
of characters is decoded and the message is shown. This may take some time as the decryption is not optimized and uses the 
basic Chinese Reminder Theorem.
