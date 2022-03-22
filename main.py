from breaking import Decryption
from cleaning import CipherTextController


def main():
    with open('cipher.txt', 'r') as cf:
        cipher_txt = cf.read()
        cipher, cipher_con = CipherTextController.from_text(cipher_txt)
    if cipher_txt is None:
        print('can not read the cipher from file')
        exit(1)

    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dec = Decryption(cipher, alphabets)
    dec.run()

    print('....')
    dec.write_result()


if __name__ == '__main__':
    main()
