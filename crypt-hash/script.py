import hashlib

print
print("Program to generate SHA-256 Hash of the string 'your mom'")
print

myString = 'your mom'
hash = hashlib.sha256()

hash.update(myString)

hexSHA256 = hash.hexdigest()

print("SHA-256 Hash: " + hexSHA256.upper())
print

print("Process Complete")