"""hand written crypto module because there is no default package"""
from hashlib import sha512
encrypted_name = "a"
digest_size = sha512().digest_size

class PictureSlices:
    def __init__(self,open_name:str):
        print("PicSlices opening %s" % open_name)
        self.file = open(open_name, "rb")

    def __iter__(self):
        return self

    def __next__(self):
        result = self.file.read(digest_size)
        if len(result) == 0:
            raise StopIteration
        else:
            return result

    def __del__(self):
        self.file.close()


def xor(a:bytes, b:bytes):
    # assert len(a) == len(b), "XOR: inputs not of equal length"
    return bytes(a_single ^ b_single for (a_single, b_single) in zip(a, b))


def decrypt_file(open_name:str, write_name:str, key:str):
    """symetric stream cipher using SHA512 function"""


    with open(write_name, "wb") as f:
        key = key.encode()
        for (i, part_of_picture) in enumerate(PictureSlices(open_name)):
            round_key = b"%d%s randominfix %d" % (i, key, i)
            decrypted_part = xor(part_of_picture, sha512(round_key).digest())
            f.write(decrypted_part)

ENCRYPT = True
enc_suffix = "_encrypted" 

if __name__ == '__main__':
    key = input("enter decryption key\n")
    files = ["pic.jpeg", "flowers.py", "rng.py", "karte.py"]

    for filename in files:
        print("processing %s" % filename)
        enc_filename = filename + enc_suffix
        if ENCRYPT:
            open_name, write_name = filename, enc_filename
        else:
            open_name, write_name = enc_filename, filename

        print("opening %s, writing %s\n" % (open_name, write_name))

        decrypt_file(open_name, write_name, key + filename)






