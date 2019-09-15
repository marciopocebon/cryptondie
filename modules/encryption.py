import os
import binascii
import pyaes

class EncryptionData():
    def __init__(self, key):
        self.key = key
        self.extension_enc = ".crypton"
        self.extension_dec = ".descrypton"
        self.remove_file = True

    def read_file(self, data):
        open_file = open(data, "rb")
        read_file_data = open_file.read()
        open_file.close()

        return read_file_data

    def rename_file(self, file_name, data):
        if self.extension_enc in file_name:
            file_name = file_name.replace(self.extension_enc, "")
            self.remove_file = False
            new_file_name = "{0}{1}".format(file_name, self.extension_dec)

        else:
            new_file_name = "{0}{1}".format(file_name, self.extension_enc)
        
        new_file = open(new_file_name, "wb+")
        new_file.write(data)
        new_file.close()

        if self.remove_file:
            os.remove(file_name)
        
        return new_file

    def encrypt(self, file_name):
        read_file_data = self.read_file(file_name)

        aes = pyaes.AESModeOfOperationCTR(self.key)
        crypto_data = aes.encrypt(read_file_data)
        crypto_data_hex = binascii.hexlify(crypto_data)

        self.rename_file(file_name, crypto_data)

    def decrypt(self, file_name):
        read_file_data = self.read_file(file_name)        

        aes = pyaes.AESModeOfOperationCTR(self.key)
        crypto_data = aes.decrypt(read_file_data)

        self.rename_file(file_name, crypto_data)
