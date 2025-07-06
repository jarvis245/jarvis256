

import uuid
import hashlib
import user_m
import sys
import getpass

""" 

*libraries :

uuid ---> uuid usable for make unique id for users .
hashlib ---> hashlib usable for hashing password when password gone on json file.  
sys ---> we can use it for exit from some while in this program. 
getpass ---> getpass usable for get input from user with hidden way.

*call another file or class methood :

user_m ---> this file made for handeling user from part of back and use api tool for open and find key,s.

*describe:

this file is main,s part of code and combine it with user_m .

*** alert *** :
pls run this file with supplement.

"""

global login_p
login_p = False 

class Main():
    
    def __init__(self):
        """ * this part does,t need describe this is init * """
        self.file = "database.json"
        self.account_inf = []
        self.dic_keyword = ["Username", "Password", "UUID", "Phone_num"]
        self.new_key_dic = ["Username","Password","UUID","Phone_num"]
        self.new_inf = []
        self.accounts = {}
        
    def creat_acount(self):
        
        """ * this part for make account in main part and get input from client * """
        
        self.username = input("enter user name: ")

        while len(self.username) == 0 :
            if len(self.username) == 0:
                self.username = input("pls feed this part : ")

            else:
                sys.exit()


        self.password = getpass.getpass("enter password: ").encode()
        self.phone = input("enter phone: ")
        
        if len(self.phone) == 0 : 
            self.final_phone = None
        else:
            self.final_phone = self.phone

        self.uuid = str(uuid.uuid4())

        self.hash_pass = hashlib.sha256()
        self.hash_pass.update(self.password)
        self.f_hash_pass = self.hash_pass.hexdigest()

        self.account_inf.append(self.username)
        self.account_inf.append(self.f_hash_pass)
        self.account_inf.append(self.uuid)
        self.account_inf.append(self.final_phone)

        while True:
            request = input("are u sure about informatin Y/n : ").upper()
            if request == "Y":
                self.accounts[self.username] = dict(zip(self.dic_keyword ,self.account_inf))
                user_m.user_managment.save_file(self, self.accounts)
                break

            elif request == "N":
                Main.creat_acount(self)
                break
            
            else:
                print("Plese Enter Y/n")

    def edit_account(self):
        """ * this part for edit account in main part and get input from client * """
        self.new_username = input("pls enter your new name : ")
        while len(self.username) == 0 :
            if len(self.username) == 0:
                self.new_username = input("pls feed this part : ")

            else:
                sys.exit()

        self.ap_hash = self.f_hash_pass
        if self.ap_hash == Main.publish_info["Password"]:
            pass
        else:
            print("your last pass not true")
            res = Main.edit_account(self)

        self.new_phone = input("pls enter new phone number :")
        
        if len(self.new_phone) == 0 : 
            self.final_new_phone = None
        else:
            self.final_new_phone = self.new_phone

        
        self.new_uuid = str(uuid.uuid4())
        self.account_inf.append(self.new_username)
        self.account_inf.append(self.ap_hash)
        self.account_inf.append(self.new_uuid)
        self.account_inf.append(self.final_new_phone)
        self.accounts[self.new_username] = dict(zip(self.dic_keyword,self.account_inf))

        print(f"old_info : {self.publish_info}")
        print(f"new_info : {self.accounts}")

                
        while True:
            request_2 = input("are u sure about informatin Y/n ?").upper()
            if request_2== "Y":
                #user_m.user_managment.delete_account(self,self.username,self.accounts)
                user_m.user_managment.edit_account(self,self.username,self.new_username,self.accounts)
                break

            elif request_2== "N":
                Main.edit_account(self)
                break
   
    def change_pass(self):

        """ * this part for change password in main part and get input from client * """

        self.username = Main.publish_info["Username"]
        self.phone = Main.publish_info["Phone_num"]
        self.uuid = Main.publish_info["UUID"]
        self.last_hash_pass = getpass.getpass("pls enter last password ").encode()
        self.hash_pass = hashlib.sha256()
        self.hash_pass.update(self.last_hash_pass)
        self.final_last_hash_pass = self.hash_pass.hexdigest()
        
        if self.final_last_hash_pass == Main.publish_info["Password"]:
            pass
        else:
            print("your last pass not true")
            res = Main.change_pass(self)

        self.new_pass = getpass.getpass("pls enter your new pass").encode()
        self.hash_new_pass = hashlib.sha256()
        self.hash_new_pass.update(self.new_pass)
        self.final_new_hash_pass = self.hash_new_pass.hexdigest()

        self.new_pass_re = getpass.getpass("pls repeat your new password : ").encode()
        self.hash_new_pass_re = hashlib.sha256()
        self.hash_new_pass_re.update(self.new_pass_re)
        self.final_new_hash_pass_re = self.hash_new_pass_re.hexdigest()



        if self.final_new_hash_pass == self.final_new_hash_pass_re:
            pass
        else:
            print("your new pass and repeat of this is not  match !")
            res = Main.change_pass(self)
        
        self.account_inf.append(self.username)
        self.account_inf.append(self.final_new_hash_pass_re)
        self.account_inf.append(self.uuid)
        self.account_inf.append(self.phone)
        self.accounts[self.username] = dict(zip(self.dic_keyword,self.account_inf))
        print(f"old_info : {self.publish_info}")
        print(f"new_info : {self.accounts}")
                
        while True:
            request_3 = input("are u sure about informatin Y/n : ").upper()
            if request_3== "Y":
                user_m.user_managment.cahnge_pass_b(self, self.username,self.accounts)
                break

            elif request_3 == "N":
                Main.change_pass(self)
                break
            
            else:
                print("Plese Enter Y/n")        

    def login(self):

        """ * this part for login in main part and get info (user,pass) from client and check it * """

        self.username = input("enter user name: ")
        while len(self.username) == 0 :
            if len(self.username) == 0:
                self.username = input("pls feed this part : ")

            else:
                sys.exit()

        self.password = getpass.getpass("enter password: ").encode()
        while len(self.password) == 0 :
            if len(self.password) == 0:
                self.password = input("pls feed this part : ")

            else:
                sys.exit()
        
        self.hash_pass = hashlib.sha256()
        self.hash_pass.update(self.password)
        self.f_hash_pass = self.hash_pass.hexdigest()
        
        info = user_m.user_managment.login(self, self.username)
        Main.publish_info = info
        
        if info == False:
            print("account dos not exists")
        else:
            self.password = Main.publish_info["Password"]

            if self.password == self.f_hash_pass:
                print("login succes")
                login_p = True
                print(login_p)
                application.account_menu()
                self.option = input("pls enter your option : ")
                res = Main.dashboard(self,self.option)
        
                

            else:
                print("password is not correct")
                res = Main.login(self)

    def main_case(self, option):

        """ * this methood for give option or switch case like c++ when clients when out login need options * """
        
        match option :
            case "1":
                return application.creat_acount()
            case "2":
                return application.login()
            case "0":
                return sys.exit()
            case _:
                return print("your choice isn,t in run list !")
            
    def dashboard(self, option):
        
        """ *this part give option or switch case like c++ when clients login to accounts or find key from json file  * """

        match option :
            case "1":
                return application.showinfo()
            case "2":
                return application.edit_account()
            case "3":
                return application.change_pass()
            case "0":
                return login_p == False
            case _:
                "..."
                
    def showinfo(self):

        """ * this part for show_info in main part for clients or users * """        
        
        print(Main.publish_info)
     
    def display_menu(self):

        """ *this part display option when clients with out login * """

        print("\nMENU:")
        print("1.add account")
        print("2.login")
        print("0.finish")
        
    def account_menu(self):

        """ *this part display option when clients login to accounts or find key from json file  * """
        
        print("***welcome your account***")
        print("\nnow u should use facilities :")
        print("1.show your,s information!")
        print("2.edit information !!")
        print("3.change password !!!")
        print("0.logout")
                    
                    

           
if __name__ == "__main__":
    
    """ *this part for run program* """
    
    while True:
        application = Main()
        choice = str(input(f"{application.display_menu()}".replace("None","--->:")))

        while bool(choice) == True:

            if login_p == False:
                application.main_case(choice)
                break
                
            elif login_p == True:
                application.account_menu
                application.dashboard(choice)
                sys.exit()

            else:
                break


