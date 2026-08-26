# PR.6 File Operator

import datetime

class journal:

    
    def add(self):
        try:
            C = "f.txt"

            entry = input("Enter your journal entry:\n")
            
            time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")
            print(time)

            with open(C,"a") as file:
                file.write(f"\n[{time}]\n")
                file.write(entry + "\n")
            
            print("\nYour Entery has sucssessfully")
        
        except Exception as e:
            
            print("Error ",e)


    def view(self):

        try:
            C = "f.txt"
            with open(C,"r") as file:

                Content = file.read()

                if Content:
                    print("\n =-=-= All Journal Entries =-=-=")
                    print(Content)
                    print("==================================\n")
                else:
                    print("\nJournal is empty!\n")

        except FileNotFoundError :
            print(" Your file is not in our Dictenary")

        except Exception as e:
            print("\nError in reading Entries:",e)

    def Search(self):

        C = "f.txt"
        D = input("\nEnter Keyword or Data for Search :")

        try:
            file = open(C,"r")
            lines = file.readlines()
            found = False

            for line in lines :
                if D.lower() in line.lower():
                    print(line)
                    found = True
            if not found:
                print("\nKeyword Don't match")

            file.close()

        except FileNotFoundError:
            print("\nFile not Found")
                
         
    def delete(self):

        try:
            C = "f.txt"

            B = input("\nYoue finally have to delete your entery (yes / No):\n")

            if B == "yes":
                

                with open(C,"w") as file:
                    ent = file.write("Contend Deleted")
                    print(ent)
                    print("Conted Deleted Successfully !!")

            elif B == "no":
                print("your Entry's are safe ")
            

            else:
                ("Enter Correct Option from Above")
                

        except FileNotFoundError :
            print(" Your file is not in our Dictenary")

        except Exception as e:
            print("Error on this path:",e)

# Mainmanu
my_journal = journal()
while True:
    print("\n==== Welcome to Personal journal Manager ====\n")
    print("\nSelecte One Option Fro Given Option\n")
    print(" 1. Add a New Entry")
    print(" 2. Viwe All Entery")
    print(" 3. Search for an Entry")
    print(" 4. Delete an Entry")
    print(" 5 Exit")

    choice=input("\nEnter your choice :")


    if choice == "1":
        my_journal.add()

    elif choice == "2":
        my_journal.view()

    elif choice == "3":
        my_journal.Search()

    elif choice == "4":
        my_journal.delete()

    elif choice == "5":
        print("Thank you for using our Personal Journal Programe")
        break

    else:
        print("Invalid input\n")    
            
            


            
        

            
