from selenium import webdriver
import time

# Open up a Firefox browser and navigate to web page.
driver = webdriver.Chrome(executable_path="/home/shuchi/Downloads/chrome webdriver/chromedriver_linux64/chromedriver")
driver.get("http://econpy.pythonanywhere.com/ex/001.html")
time.sleep(4)

# Extract lists of "buyers" and "prices" based on xpath.
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# Print out all of the buyers and prices on page:
num_page_items = len(buyers)
for i in range(num_page_items):
    print(buyers[i].text + " : " + prices[i].text)

# Clean up (close browser once completed task).
driver.close()
print("Test completed")
