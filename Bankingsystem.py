import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="T3chBunny!33"
)

print(mydb)
mycursor = mydb.cursor()

while True:


  print("========== WELCOME TO BANKING SYSTEM ==========")
  print("************************************************************")
  print("========== (a). Open New Account ============")
  print("========== (b). The Withdraw Money ============")
  print("========== (c). Deposit Money ============")
  print("========== (d). Check Balance ============")
  print("========== (e). Close Account ============")
  print("========== (f). Quit ============")
  print("************************************************************")



  
  EnterLetter = input("Select a Letter from the Above Box menu : ")
  if EnterLetter== "f":
    print ("Thanks, hope to see you soon!")
    break
  if EnterLetter == "a":
    print(" Letter a is Selected by the Client")
  #NumberOfClient = eval(input("Number of Clients : "))
  #u = u + NumberOfClient


    NameInfo= input("Create User Name : ")
    PinInfo= input (" Create New Pin Number : ")
    AccountNumber = random.randint(0, 100000)
    print(f"Your account number is : {AccountNumber}")



    sql = "INSERT INTO bankingsystem.bank (UserName, PinNumber, AccountNumber,Balance) VALUES (%s, %s, %s,%s)"
    val = (NameInfo, PinInfo,AccountNumber,0)
    mycursor.execute(sql, val)
    mydb.commit() 

