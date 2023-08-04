import json

class Database_:

    def __init__(self):

        with open("db.json",'r') as f:

            self.db=json.load(f)

    def add(self,name,email,password):

        if email in self.db:
            return 0
        else:
            self.db[email]=[name,password]
            with open('db.json','w') as f:
                json.dump(self.db,f)

            return 1
        
    def login(self,email,password):

        if self.db[email][1]==password:
            return 1
        else:
            return 0




