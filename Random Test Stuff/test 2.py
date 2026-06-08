import hashlib
userinput = input("gib")
password = hashlib.sha256(f"{bytes(userinput)}")
print(password.hexdigest())