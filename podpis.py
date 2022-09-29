
import rsa

(pubkey, privkey) = rsa.newkeys(512)

with open('output.txt', mode='rb') as privatefile:
    signature = rsa.sign(privatefile, privkey, 'SHA-256')
    hash = rsa.compute_hash(privatefile, "SHA-256")
    signature = rsa.sign_hash(hash, privkey, "SHA-256")
    
    print(rsa.verify(privatefile, signature, pubkey))