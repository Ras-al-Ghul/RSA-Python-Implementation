# RSA Cryptography implementation in Python

This is a basic Python code to implement RSA Cryptography. The aim was to learn to code in Python and to learn about the RSA Cryptosystem.
 
### To execute

- Firstly, Prime numbers are genereted using `primegeneration.py`. 
- The generated data is then inserted wherever necessary (see below) in the `encryption.py` and `decryption.py` files. The prime numbers generated are not huge though they are each around 8 digits long. But for an illustration this serves the purpose. The prime number generation can be made faster using Rabin-Miller Primality testing.
- The `encryption.py` file is to be run next. Before that one has to paste the `public key` as `ekey` and the `modulus` as `modulus` (both at the top of the `encryption.py` file) from the `primegeneration.py` execution. 
- The text to be encrypted is input. At present only alphabets, digits and spaces are supported. One can modify that. 
- Then padding is done to further show how it is done in the real world. 
- Then the message is encrypted and converted to hexadecimal text. The output is a hexadecimal stream of characters.
- Then one has to provide this stream of characters as input for the `decryption.py` file but...
- But firstly one has to copy the values of `private key` as `dkey`, `modulus` as `modulus`, `prime numbers`, `p` as `p` and `q` as `q` (all at the top of the `decryption.py` file) from the earlier `primegeneration.py` execution.
- Then after providing the input, the stream of characters is decoded and the message is shown. This may take some time as the decryption is not optimized and uses the 
basic Chinese Reminder Theorem.

So the commands and the order of execution is :

- `python primegeneration.py`
- `python encryption.py`
- `python decryption.py`
