print("=== PASSWORD VALIDATOR ===")
while True:
  password = input("\nEnter a password: ")

  upper = False
  lower = False
  number = False
  
for char in password:
    if char >= "A" and char <= "Z":
        upper = True
    if char >="a" and char <= "z":
        lower = True
    if char >= "0" and char <= "9":
        number = True
valid = True

if len(password) < 8:
  print("Password must have at least 8 characters.")
  valid = False
  
if upper == False:
    print("Password must contain an uppercase letter.")
    
if lower == False:
    print("Password must contain an lowercase letter.")
    
if number == False:
    print("Password must contain a number.")

if valid == True:
  print("\nPassword is valid!")
  break
