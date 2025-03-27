import hashlib

def text_to_sha256(text):
    # Encode the text to bytes
    text_bytes = text.encode('utf-8')
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the bytes
    sha256_hash.update(text_bytes)
    # Get the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

passwords = [
    "G5#hT8@q",
    "m2$Jk4!z",
    "R1^pL7*e",
    "t9&Vb3#Y",
    "W8@xF6!j",
    "c4*Qw2$H",
    "N3^zK5#r",
    "j7!Lp1@M",
    "D6&fT9^s",
    "a2#Xy8!Q",
    "P5@kR3*z",
    "h1^Vn4!J",
    "S8$wB2#t",
    "e3*Zq7@L",
    "K9!mF5^x"
]

# Example usage: print the list of passwords
for password in passwords:
    print(text_to_sha256(password))
