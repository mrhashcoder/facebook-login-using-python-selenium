from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
  
browser = webdriver.Chrome('driver')
browser.get("http://www.facebook.com")
  
username = browser.find_elements_by_xpath('//*[@id="email"]')
password = browser.find_elements_by_xpath('//*[@id="pass"]')
submit   = browser.find_elements_by_xpath('//*[@id="u_0_a"]')
#put yourusername of facebook at your username and password at your password
# make sure that driver and .py file be at same directory

  
username[0].send_keys("YOUR USERNAME")
password[0].send_keys("YOUR PASSWORD")
  

submit[0].click()
  

wait = WebDriverWait( browser, 5 )
  
try:
    page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)

except TimeoutException:
    self.fail("Loading timeout expired")    
    self.assertEqual(browser.current_url,correct_page,msg = "Successful Login")