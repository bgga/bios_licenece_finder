import os

import binascii

file_list = []

finded = 0

w = open("klucze.txt", "a+")
w.close()

for x in os.listdir("pliki"): 
    if x.endswith(".bin"):
        file_list.append(x)

for file in file_list:
    with open("pliki/"+file, "rb") as f:
        content = f.read()

    with open("klucze.txt", "r") as k:
        klucze = k.read()

    hex_bytes = str(binascii.hexlify(content))
    fraza = "010000000000000001000000000000001d000000"
    index = hex_bytes.find(fraza)

    if fraza in hex_bytes:

        key_hex = hex_bytes[index+40:index+98]
        decoded_hex = str(binascii.unhexlify(key_hex))
        decoded_hex_cut = decoded_hex[2:31]

        if decoded_hex_cut in klucze:
            print(f"{file}: Key allready in database")

        else:
            print(f"{file}: Found KEY! ----> {decoded_hex_cut}")
            with open("klucze.txt", "a") as klucze:
                klucze.write(decoded_hex_cut+"\n")
            finded += 1 
                           
    else:
        print(f"{file}: Key not Found!")

filescount = len(file_list)

print(f"Przeszukano: {filescount} plików, znaleziono: {finded} kluczy.")

