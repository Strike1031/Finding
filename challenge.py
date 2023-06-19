from codecs import backslashreplace_errors
from functools import cache
from json import JSONDecodeError
from platform import java_ver
from progressbar import ProgressBar, Percentage, Bar, ETA
from pprint import pprint
import blocksmith, time, sys, os, uuid, datetime
from dotenv import load_dotenv
from etherscan import Etherscan
from pathlib import Path
import random

load_dotenv()
eth = Etherscan(os.environ.get("ETHERSCAN_API_KEY"))
#Start private address  example:0x3f3493044924290290290902492... (64byte)
#basic_startPrivateKey = 0xbfd1054b382a415fa4e52efd9d21657f9382c9d89f9933f46457a1a225852535

# Define global (non .env) variables
pbar = ProgressBar()
savedAddresses = []
savedKeys = []

##############################################
#     Functions from Blocksmith Library      #
##############################################
def generatePrivateKey():
    # Generate Private Key
    kg = blocksmith.KeyGenerator()
    kg.seed_input('since rule enact rally actress weasel chapter ivory ensure entire flock exchange')
    key = kg.generate_key()
    return key

def privateKeyToBitcoinWallet(key):
    # Create Bitcoin wallet from private key
    address = blocksmith.BitcoinWallet.generate_address(key)
    return address
    

def privateKeyToEthereumWallet(key):
    # Create Ethereum wallet from private key
    address = blocksmith.EthereumWallet.generate_address(key)
    checksum_address = blocksmith.EthereumWallet.checksum_address(address)
    return checksum_address


##############################################
#   Finging Valueable Wallets   #
##############################################
def finding(unique_filename="Find.txt", printVals=False, saveAll=False):
    try:    
        with open(unique_filename, 'w') as outFile:
            print("Finding...")
            # for i in pbar(range(amount)):
            z = 0
            while True:
                z += 1
                print(str(z))
                #print(count)
                # privateKey = generatePrivateKey()
                time.sleep(random.uniform(0, 1.0)) #after random seconds between a range
                c1 = str(random.choice('0123456789abcdefABCDEF'))
                c2 = str(random.choice('0123456789abcdefABCDEF'))
                c3 = str(random.choice('0123456789abcdefABCDEF'))
                c4 = str(random.choice('0123456789abcdefABCDEF'))
                c5 = str(random.choice('0123456789abcdefABCDEF'))
                c6 = str(random.choice('0123456789abcdefABCDEF'))
                c7 = str(random.choice('0123456789abcdefABCDEF'))
                c8 = str(random.choice('0123456789abcdefABCDEF'))
                c9 = str(random.choice('0123456789abcdefABCDEF'))
                c10 = str(random.choice('0123456789abcdefABCDEF'))
                c11 = str(random.choice('0123456789abcdefABCDEF'))
                c12 = str(random.choice('0123456789abcdefABCDEF'))
                c13 = str(random.choice('0123456789abcdefABCDEF'))
                c14 = str(random.choice('0123456789abcdefABCDEF'))
                c15 = str(random.choice('0123456789abcdefABCDEF'))
                c16 = str(random.choice('0123456789abcdefABCDEF'))
                c17 = str(random.choice('0123456789abcdefABCDEF'))
                c18 = str(random.choice('0123456789abcdefABCDEF'))
                c19 = str(random.choice('0123456789abcdefABCDEF'))
                c20 = str(random.choice('0123456789abcdefABCDEF'))
                c21 = str(random.choice('0123456789abcdefABCDEF'))
                c22 = str(random.choice('0123456789abcdefABCDEF'))
                c23 = str(random.choice('0123456789abcdefABCDEF'))
                c24 = str(random.choice('0123456789abcdefABCDEF'))
                c25 = str(random.choice('0123456789abcdefABCDEF'))
                c26 = str(random.choice('0123456789abcdefABCDEF'))
                c27 = str(random.choice('0123456789abcdefABCDEF'))
                c28 = str(random.choice('0123456789abcdefABCDEF'))
                c29 = str(random.choice('0123456789abcdefABCDEF'))
                c30 = str(random.choice('0123456789abcdefABCDEF'))
                c31 = str(random.choice('0123456789abcdefABCDEF'))
                c32 = str(random.choice('0123456789abcdefABCDEF'))
                c33 = str(random.choice('0123456789abcdefABCDEF'))
                c34 = str(random.choice('0123456789abcdefABCDEF'))
                c35 = str(random.choice('0123456789abcdefABCDEF'))
                c36 = str(random.choice('0123456789abcdefABCDEF'))
                c37 = str(random.choice('0123456789abcdefABCDEF'))
                c38 = str(random.choice('0123456789abcdefABCDEF'))
                c39 = str(random.choice('0123456789abcdefABCDEF'))
                c40 = str(random.choice('0123456789abcdefABCDEF'))
                c41 = str(random.choice('0123456789abcdefABCDEF'))
                c42 = str(random.choice('0123456789abcdefABCDEF'))
                c43 = str(random.choice('0123456789abcdefABCDEF'))
                c44 = str(random.choice('0123456789abcdefABCDEF'))
                c45 = str(random.choice('0123456789abcdefABCDEF'))
                c46 = str(random.choice('0123456789abcdefABCDEF'))
                c47 = str(random.choice('0123456789abcdefABCDEF'))
                c48 = str(random.choice('0123456789abcdefABCDEF'))
                c49 = str(random.choice('0123456789abcdefABCDEF'))
                c50 = str(random.choice('0123456789abcdefABCDEF'))
                c51 = str(random.choice('0123456789abcdefABCDEF'))
                c52 = str(random.choice('0123456789abcdefABCDEF'))
                c53 = str(random.choice('0123456789abcdefABCDEF'))
                c54 = str(random.choice('0123456789abcdefABCDEF'))
                c55 = str(random.choice('0123456789abcdefABCDEF'))
                c56 = str(random.choice('0123456789abcdefABCDEF'))
                c57 = str(random.choice('0123456789abcdefABCDEF'))
                c58 = str(random.choice('0123456789abcdefABCDEF'))
                c59 = str(random.choice('0123456789abcdefABCDEF'))
                c60 = str(random.choice('0123456789abcdefABCDEF'))
                c61 = str(random.choice('0123456789abcdefABCDEF'))
                c62 = str(random.choice('0123456789abcdefABCDEF'))
                c63 = str(random.choice('0123456789abcdefABCDEF'))
                c64 = str(random.choice('0123456789abcdefABCDEF'))
                magic = (
                    c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 + c20 + c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30 + c31 + c32 + c33 + c34 + c35 + c36 + c37 + c38 + c39 + c40 + c41 + c42 + c43 + c44 + c45 + c46 + c47 + c48 + c49 + c50 + c51 + c52 + c53 + c54 + c55 + c56 + c57 + c58 + c59 + c60 + c61 + c62 + c63 + c64)
                privateKey = str(magic)
                #print("Prviate key: ", privateKey)
                walletAddress = privateKeyToEthereumWallet(privateKey)
                #print('public key: ', walletAddress)
                if printVals == True:
                    print(f"{walletAddress}\t:\t{privateKey}")
                #if saveAll == True:
                    #savedAddresses.append(walletAddress)
                    #savedKeys.append(privateKey)
                # If you want to check individual balances as you generate them, use the following block of code
                try:
                    balance = eth.get_eth_balance(walletAddress)
                    #print(balance)
                    if balance != '0':
                        print("Ether detected!!!!!!!!!!!!!!!!")
                        print("Wallet: ", walletAddress)
                        print("Private Key: ", privateKey)
                        print("Balance: ", balance)
                        #savedAddresses.append(walletAddress)
                        #savedKeys.append(privateKey)
                        outFile.write("\nWALLET FOUND")
                        outFile.write(f"\nWallet Address: {walletAddress}")
                        outFile.write(f"\nPrivate Key: {privateKey}")
                except JSONDecodeError:
                    # If you would like to track how many API calls fail (due to your limit being exceeded or some other issue) you can put your logic here
                    #balanceCheckFailCount = balanceCheckFailCount + 1
                    pass
    except:
        pass        


if __name__ == '__main__':
    currentDT = datetime.datetime.now()
    filename = str(currentDT.year)+"_"+str(currentDT.month)+"_"+str(currentDT.day)+"_"+str(currentDT.hour)+"_"+str(currentDT.minute)+"_"+str(currentDT.second)
    filename = "collection\\" + filename + ".txt"
    finding(filename)