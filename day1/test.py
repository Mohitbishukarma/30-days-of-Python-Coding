import passValidator
password=input("Enter Password : ")
print(passValidator.passCheck(password))

# test cases:
# password=JacK123@xdg$ >>True
# password=jack123@xdg$ >>False
# password=JaCk@xdg$ >>False
# password=JAck123xdg$ >>False
# password=Jack123xdg$ >>False
# password=Jack1xdg$ >>False
# password=JaCk12xD*g@$ >>False


