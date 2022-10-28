"""
 Author: Arman Kompany Zare - 300031228 - akomp033@uottawa.ca
 Written in Python 3.10

 *Please install pandas with: `pip install pandas`
  before running.
"""

import random
import pandas

# Keys for each layer
k1 = 33219
k2 = 12812
k3 = 3687
k4 = 8620
k5 = 33919

# 4x4 Sbox used in Q2
Sbox = {
    0: 2,
    1: 5,
    2: 0,
    3: 9,
    4: 13,
    5: 14,
    6: 7,
    7: 15,
    8: 1,
    9: 8,
    10: 3,
    11: 6,
    12: 4,
    13: 11,
    14: 12,
    15: 10
}

# Respective Inverse 4x4 Sbox
iSbox = {value: key for key, value in Sbox.items()}

# Permutation Mapping
Perm = {
    0: 0,
    1: 4,
    2: 8,
    3: 12,
    4: 1,
    5: 5,
    6: 9,
    7: 13,
    8: 2,
    9: 6,
    10: 10,
    11: 14,
    12: 3,
    13: 7,
    14: 11,
    15: 15
}

# converts int to binary string of length x
def int2bin(input, x):
    result = bin(input)[2:]
    leading_zeroes = ""
    for i in range(x-len(result)):
        leading_zeroes += "0"
    return leading_zeroes + result

# converts binary string to int
def bin2int(input):
    return int(input, 2)

# takes 4-bit string input and converts to 4-bit string output using the declared Sbox
def SboxFunc4B(input):
    return int2bin(Sbox[bin2int(input)], 4)

# takes 16-bit string input and converts to 16-bit string output using the declared Sbox
def SboxFunc16B(input):
    return SboxFunc4B(input[0:4]) + SboxFunc4B(input[4:8]) + SboxFunc4B(input[8:12]) + SboxFunc4B(input[12:16])

# takes 4-bit string input and converts to 4-bit string output using the declared iSbox
def iSboxFunc4B(input):
    return int2bin(iSbox[bin2int(input)], 4)

# takes 16-bit string input and converts to 16-bit string output using the declared iSbox
def iSboxFunc16B(input):
    return iSboxFunc4B(input[0:4]) + iSboxFunc4B(input[4:8]) + iSboxFunc4B(input[8:12]) + iSboxFunc4B(input[12:16])

# takes 4-bit string input and converts to 4-bit string output using the declared Permutation map
def PermFunc16B(input):
    result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(16):
        result[Perm[i]] = input[i]
    return ''.join(result)

# An encryption function which takes a 16-bit Plaintext integer and gives back a 16-bit Ciphertext integer
# Goes through the entire SPD
def SPDFullEncrypt(p):

    u1 = p ^ k1
    v1 = bin2int(SboxFunc16B(int2bin(u1, 16)))
    #print("U1 = "+int2bin(u1, 16))
    #print("V1 = "+int2bin(v1, 16))

    u2 = bin2int(PermFunc16B(int2bin(v1, 16))) ^ k2
    v2 = bin2int(SboxFunc16B(int2bin(u2, 16)))
    #print("U2 = "+int2bin(u2, 16))
    #print("V2 = "+int2bin(v2, 16))

    u3 = bin2int(PermFunc16B(int2bin(v2, 16))) ^ k3
    v3 = bin2int(SboxFunc16B(int2bin(u3, 16)))
    #print("U3 = "+int2bin(u3, 16))
    #print("V3 = "+int2bin(v3, 16))

    u4 = bin2int(PermFunc16B(int2bin(v3, 16))) ^ k4
    v4 = bin2int(SboxFunc16B(int2bin(u4, 16)))
    #print("U4 = "+int2bin(u4, 16))
    #print("V4 = "+int2bin(v4, 16))

    output = v4 ^ k5

    return output

# Takes any 4x4 Sbox as input and generates a Differential Distribution Table
def DiffDistTable(Sbox):
    table = [[16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for XDiff in range(1, 16):
        for YDiff in range(1,16):
            counter = 0
            tmp = []
            for X1 in range(16):
                X2 = XDiff ^ X1
                Y1 = Sbox[X1]
                Y2 = Sbox[X2]
                compVal = Y1 ^ Y2
                if compVal == YDiff:
                    counter += 1
            table[XDiff][YDiff] = counter

    return table


# --- Main Program ---


inputList = random.sample(range(2**16), 5000) # Generating 5000 random 16-bit ints
rightPairs = []
for i in inputList: # Generating respective right pairs for each random int
    rightPairs.append((i, i^160)) # U1 = 160 = 0000000010100000


rightPairsFinalOutputDiff = [] # Generating Output Differentials
for i in rightPairs:
    rightPairsFinalOutputDiff.append(SPDFullEncrypt(i[0]) ^ SPDFullEncrypt(i[1]))

U4 = 4097 # = 0001000000000001
table = [[0 for x in range(2)] for y in range(256)] # Creating an empty 256x2 Probability table

for key in range(256): # Generating Probability table
    table[key][0] = key
    count = 0
    for outputDiff in rightPairsFinalOutputDiff:
        binOutput = int2bin(outputDiff, 16)
        binKey = int2bin(key, 16)
        outputLeftSeg = binOutput[0:4]
        outputRightSeg = binOutput[12:16]
        keyLeftSeg = binKey[0:4]
        keyRightSeg = binKey[12:16]

        finalLeftSeg = iSboxFunc4B(int2bin((bin2int(keyLeftSeg) ^ bin2int(outputLeftSeg)), 4))
        finalRightSeg = iSboxFunc4B(int2bin((bin2int(keyRightSeg) ^ bin2int(outputRightSeg)), 4))

        final = bin2int(finalLeftSeg + "00000000" + finalRightSeg)
        if final == U4:
            count += 1
    table[key][1] = count/5000

# Sorting table data based on Probability
table = sorted(table, key=lambda x: x[1], reverse = True)
pandas.set_option('display.max_rows', None)
df = pandas.DataFrame(table)
print(df)

# Sample optional input
input = 999
print("Plaintext: " + int2bin(input, 16))
print("Ciphertext: " + int2bin(SPDFullEncrypt(input), 16))

# Print Differential Distribution table based on given Sbox
print("Differential Distribution Table:\n")
print(pandas.DataFrame(DiffDistTable(Sbox)))
