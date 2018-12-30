#Password Manager
import os
def main():
    key = True
    while key :
        inputFile = input("Enter name of the file to add passwords:")+".txt"
        if os.path.isfile(inputFile):
            inFile = open(inputFile,"a")
            thisDict = {"Account": "user", "Password":"default"}
            while len(thisDict.get("Account")) != 0:
                thisDict["Account"]= input("Enter the account to add or leave empty to finish:")
                if len(thisDict.get("Account")) == 0 :
                    pass
                else:
                    thisDict["Password"]= input("Enter the password of "+ thisDict.get("Account")+":")
                    inFile.write(thisDict.get("Account") + ":" + thisDict.get("Password")+ "\n")
            inFile.close()
            key= False


        else:
            print("Error. Invalid Filename.")
main()
