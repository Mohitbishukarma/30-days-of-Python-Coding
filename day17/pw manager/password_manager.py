import sys
import pyperclip
import os


accounts = {

}

# accounts
accounts_file = os.path.dirname(os.path.abspath(__file__))+"\\accounts.txt"
with open(accounts_file, 'r') as fptr:
    data = fptr.readlines()
    for each in data:
        account, password = each.replace("\n", "").strip().split(",")
        accounts.setdefault(account.strip(), password.strip())
    fptr.close()
    

error_msg = "Invalid Command\nUsuage:\n[account] -> to see password of account\n[account] copy -> to copy the account password\n[add] [account] [password] -> to add new account" 

# checking command line argument is passed or not
if len(sys.argv) < 2:
    print(error_msg)
    sys.exit()


if len(sys.argv) == 2:
    if sys.argv[1] in accounts:
        print(f"Account: {sys.argv[1]}   Password: {accounts.get(sys.argv[1])}")
    else:
        print("There is no account named "+sys.argv[1])

elif len(sys.argv) == 3:
    if sys.argv[1] in accounts and sys.argv[2] == "copy":
        pyperclip.copy(accounts.get(sys.argv[1]))
        print("Your password is copied to clipboard")
    else:
        if sys.argv[1] not in accounts:
            print("There is no account named "+sys.argv[1])
        elif sys.argv[2] != "copy":
            print(error_msg)

elif len(sys.argv) == 4:
    if sys.argv[1] == "add":
        # accounts.setdefault(sys.argv[2], sys.argv[3])
        with open(accounts_file, 'a') as fptr:
            fptr.write(f"{sys.argv[2]},{sys.argv[3]}\n")
            fptr.close()
        print("Your new password is added.")
    else:
        print(error_msg)

