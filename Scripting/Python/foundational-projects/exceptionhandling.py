# prompt for username
try:
    username = input("Enter username:")
    assert username.isalpha()
except:
    raise ValueError("Incorrect username!")
else:
    print("Your name:", username)
finally:
    print("Thank you.")

# prompt for password
try:
    password = input("Enter password:")
    assert password.isalnum()
except:
    raise ValueError("Incorrect password!")
else:
    print("Access granted.")
    print("Welcome", username)
finally:
    print("Have a nice day.")
