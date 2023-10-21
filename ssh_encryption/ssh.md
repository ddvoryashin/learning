SSH is a cryptographic network protocol for operating network services securely over an unsecured network.[1] It is based on public-key (asymmetrical) cryptography for authentication.

Public-key (asymmetrical) encryption uses pairs of keys: public and private ones. Both of the keys are created by a user, then a public one can be shared with a server, private key must be always hidden from anyone and shouldn't be transferred to other devices.

One of the key components of SSH is an encrypting algorithm. These algoritms are often used in SSH:
1) RSA;
2) Diffie Hellman.

How RSA works on example of Bob wanting to send a message to Alice:
1) Alice is generating public and private keys:
    1) Randomly choose two large prime numbers _**p**_ and _**q**_;
    2) Calculate _**n** = p*q_, where n is modulus for public and private keys;
    3) Calculate _**λ(n)**_. We will not dive into it here;
    4) Choose _**e**_ such, that _2 < e < λ(n)_. _e_ and _λ(n)_ are coprime (the only positive integer that is a divisor of both of them is 1);
    5) Count _**d** ≡ e<sup>−1</sup>_(mod _λ(n)_);
    6) Public key consists of _n_ and _e_. Private key consists of _n_ and _d_.
2) Alice sends the public key to Bob;
3) Bob encrypting a message, using Alice's public key _(n, e)_:
    1) We have _**M**_ - a plain unencrypted text, which we want to transfer to other server;
    2) We add a padding to _M_ and name it as _**m**_;
    3) Get encoded message: _c ≡ m<sup>e</sup>_ (mod _n_).
4) Bob send encrypted message to Alice;
5) Alice decrypts the message: _c<sup>d</sup> ≡ (m<sup>e</sup>)<sup>d</sup> ≡ m_ (mod _n_). The magic is in _d_: if we raise _m_ to the power of _d_, we get initial unencrypted message.

Example:
1) Choose _p_ = 61 and _q_ = 53;
2) Compute _n_ = 61 * 53 = 3233;
3) Compute _λ(n)_ = 780;
4) Choose _e_ such that _2 < e < λ(n)_: 17;
5) Compute d = 413, because 1 = (17 * 413) mod 780;
6) Public key is (3233, 17), and encrypting function is: _c(m) = m<sup>e</sup>_ mod _n_ = _m_<sup>17</sup> mod 3233. Private key is (3233, 413), ad decrypting function is: _m(c) = c<sup>d</sup>_ mod _n_ = _c_<sup>413</sup> mod 3233;
7) For example, _m_ = 65, then c = 65<sup>17</sup> mod 3233 = 2790, and m = 2790<sup>413</sup> mod 3233 = 65.