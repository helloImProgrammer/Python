from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:/Users/cihan/OneDrive/Masaüstü/code/python_denemeler/BTK/selenium/chromedriver.exe')
url = "https://www.youtube.com/"

driver.get(url)

time.sleep(1)
driver.maximize_window()

time.sleep(1)
searchInput = driver.find_element_by_name("search_query")

searchInput.send_keys("Şehinşah Milyon")
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
time.sleep(1)

video = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a")
video.send_keys(Keys.ENTER)

time.sleep(7)
reklam = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[15]/div/div[3]/div/div[2]/span/button")
reklam.click()

time.sleep(15)

driver.close()