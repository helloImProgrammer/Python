import requests



class Github : 
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "57a35c01d0011cc9d306ee9831930322a95cba1f"
    def user (self,username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()
    def getRepo(self,username):
        response = requests.get(self.api_url+ "/users/" + username+"/repos")
        return response.json()
    def createRepo(self,name):
        response = requests.post(self.api_url+"/user/repos?access_token="+self.token ,json=
            {
             "name": name,
                "description": "This is your first repository",
                "homepage": "https://github.com",
                "private": False,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True
                })
        return response.json()
git = Github()
while True :
    operation  = input("1-/Find User \n2-/Get Repositories \n3-/Create Repositories \n4-/Exit")

    if operation == "4" :
        break
    else : 
        if operation == "1" :

            username = input('Username : ')

            result = git.user(username)
            print("profile".center(50,"*"))
            print(f"\nname : {result['name']} \nrepo : {result['public_repos']} \nfollowers : {result['followers']}\n")
            print("*"*50)

        elif operation == "2" :
            username = input('Username : ')
            repos = git.getRepo(username)
            for repo in repos : 
                print(repo['name'])
        elif operation == "3" :
            name = input("repo name : ")
            result = git.createRepo(name)
            print(result)
        else :
            print("Hatalı tuşlama yaptınız.")