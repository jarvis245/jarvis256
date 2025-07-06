import os
import json

'''
*this file for backend file of main and manage user:

json ---> use this lib for API,s tool and make .
os ---> use this lib for open and close in python and work on file. 

'''

def search_key(data, key):

    """ * this part for search key of dict from json file *"""

    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                return v
            elif isinstance(v, (dict, list)):
                result = search_key(v, key)
                if result:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = search_key(item, key)
            if result:
                return result
    return False


class user_managment():

    """ * this class methood part of back for open,save,delete,edit,change,show * """
        
    def save_file(self, account):
        
        """ * this methood part of back for make user and save it on database or json file or account  * """
        
        if os.path.exists(self.file):
            with open(self.file,"r") as file:
                try:
                    self.old_data = json.load(file)
                except json.JSONDecodeError:
                    self.old_data = {}
                        
        else:
            self.old_data = {}
                        
        username = list(account.keys())[0]

        if username in self.old_data:
            print(f"your user '{username}'has been exist.")
            return False

        self.old_data.update(account)

        with open(self.file, "w") as file:
            json.dump(self.old_data, file, indent=2)

            print(f"your user {username} has been confirm ")
            return True

    def edit_account(self,username,new_username, account):
        """Update account, delete last account, and avoid duplicates."""
        if os.path.exists(self.file):
            with open(self.file, "r") as file:
                try:
                    self.old_data = json.load(file)
                except json.JSONDecodeError:
                    self.old_data = {}
        else:
            self.old_data = {}

        new_username = list(account.keys())[-1]
        if new_username in self.old_data:
            print(f"User '{new_username}' already exists.")
            return False

        if username in self.old_data:
            username = list(self.old_data.keys())[-1]
            del self.old_data[username]

        self.old_data.update(account)

        with open(self.file, "w") as file:
            json.dump(self.old_data, file, indent=2)
            print(f"Account '{new_username}' has been added/updated successfully.")
            return True

    def cahnge_pass_b(self,username,account) :

        """ * this methood part of back for change password and save on json file(database.json) * """

        if os.path.exists(self.file):
            with open(self.file,"r") as file:
                try:
                    self.old_data = json.load(file)
                except json.JSONDecodeError:
                    self.old_data = {}
                        
        else:
            self.old_data = {}

        username = list(account.keys())[0]
        if username in self.old_data:
            del self.old_data[username]
        
        self.old_data.update(account)
        
        with open(self.file, "w") as file:
            json.dump(self.old_data, file, indent=2)
            print(f"your new update '{username}' has been confirm ")
            return True

    def login(self, username):

        """ * this methood is part of back for find key from json file and login with this * """

        if os.path.exists(self.file):
            with open(self.file,"r") as file:
                try:
                    self.data = json.load(file)
                except json.JSONDecodeError:
                    self.data = {}
                        
        else:
            self.data = {}
            
        result = search_key(self.data, username)
        return result
    
    def load_info(self, username):
        
        """ * this part does,n have describe because its name describe it ."""
        
        if os.path.exists(self.file):
            with open(self.file,"r") as file:
                try:
                    self.data = json.load(file)
                except json.JSONDecodeError:
                    self.data = {}
                        
        else:
            self.data = {}
            
        search_key(self.data, username)