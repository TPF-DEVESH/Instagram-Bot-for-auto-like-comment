#----------------------------
#						    |
# Instagram Bot- Devesh Kr. Verma 
# instagram- @felon_tpf	
#							|
#----------------------------

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string
from time import sleep
from selenium import webdriver
#Change this list to your wanted comments (what you wnat to comment on posts)
comments = ['Please Visite on my page take a look if you like please follow ', 'Nice post- just follow me @eyetunities ', 'loool very nice!-want to earn money just follow me @eyetunities ', 'I like it!-follow me for daily motivational post on your wall', 'Super ;)-follow me guys @eyetunities ', 'hmmm,interesting-follow me for daily money earning tips ', ' wow- follow me for online money earning tips ', 'amazing post dude-also check out my profile , for Online money earning tips  ', 'learn something new - follow me @eyetunities ', 'Mind blowing - follow for money earning tips Online money  ', 'I like it , great post- follow my page please -daily money earning tips ', ]

#This variables to keep tracking of the posts 
posts=0

#Chromedriver path. Make sure to have the same Chromedriver version as your Google Chrome browser
browser = webdriver.Chrome(executable_path= r"D:\pythonlearn\python_projects\chromedriver.exe")  # <----- ENTER PATH HERE 

browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
sleep(2) 
	

def likeAndComm(): # Likes and Comments the first 9 posts
	global posts
	for y in range (1,4):
		for x in range(1,4):
			post = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/div/div['+str(y)+']/div['+str(x)+']') 
			browser.implicitly_wait(1) 
			post.click()
			sleep(2)
			postLike = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]').click()
			#postLike.click()
			print("Post liked") 
			sleep(2)
			#comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form').click() 
			print("click1")
			sleep(3)
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form').click() 
			print("click2")
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(random.choice(comments))	
			print("send1-Writing comment")
			sleep(3)
			sendComment = browser.find_element_by_xpath("//button[@type='submit']") 
			sendComment.click()
			print("click3-Comment-posted")
			print("searching for new post, searching...")
			sleep(4)
			posts+=1
			closePost=browser.find_element_by_xpath('/html/body/div[4]/div[3]/button/div')
			closePost.click()
			sleep(3)
		print ('No. of posts: ' +str(posts))
	
	sleep(5)
	browser.get('https://www.instagram.com/explore/')
	sleep(6)
	likeAndComm()
	
		
def start():
	
	username = browser.find_element_by_name('username')
	username.send_keys('Username')            # <- INSERT YOUR INSTAGRAM USERNAME HERE
	password = browser.find_element_by_name('password')
	password.send_keys('Password')            # <- INSERT YOUR INSTAGRAM PASSWORD HERE
	nextButton = browser.find_element_by_xpath("//button[@type='submit']")
	nextButton.click()
	sleep(4)
	notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
	notification.click()
	browser.get('https://www.instagram.com/explore/')
	sleep(6)
	likeAndComm() # likeAndComm function 
	sleep(5)
	
	
#Start the programm
start()
