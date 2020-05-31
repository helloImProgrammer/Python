from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from insta_user import username,password
import time

class insta :
    def __init__(self,username,password):
        self.username = username 
        self.password = password
        self.driver =  webdriver.Chrome(executable_path='C:/Users/cihan/OneDrive/Masaüstü/code/python_denemeler/BTK/selenium/chromedriver.exe')
        self.followers = [] 
        
    def login(self):
        
        self.driver.get("https://www.instagram.com/?hl=tr")
        time.sleep(3)
        self.usernameInput = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        self.usernameInput.send_keys(self.username)
        self.passwordInput = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        self.passwordInput.send_keys(self.password)
        self.button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
        self.button.click()
        time.sleep(3)
        

    def followersList(self) :
        
        self.driver.get(f"https://www.instagram.com/{self.username}/?hl=tr")
        time.sleep(5)
        self.buttonfollowers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        self.buttonfollowers.click()

        time.sleep(5)

        dialog = self.driver.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))


        action = webdriver.ActionChains(self.driver)

        while True :        # döngüye girdiğinde eğer followersCount == newFollowesCount değil ise 
                            # newFollowersCount followersCount a atanır yani yeni aşşağı indikçe yeni takipçiler hala veritabanından yükleniyor
            dialog.click()
            time.sleep(2)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:

                followerCount = newCount

                print(f"second count: {newCount}")

                time.sleep(1)

            else:

                break


        followers = dialog.find_elements_by_css_selector("li")

        for user in followers : 

            link = user.find_element_by_css_selector("a").get_attribute("href")

            print(link)
                    

insta2 = insta(username,password)
insta2.login()
insta2.followersList()




