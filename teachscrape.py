from selenium import webdriver
import time
chrome_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)


driver.get("http://www.associationofchemistryteachers.org/MembersDirectories.aspx")

review= driver.find_element_by_id("dListItems_ctl00_lblFullName")
#print(type(review))
print(review.text)
#for post in review:
#    print(post.text)

driver.find_element_by_xpath('//*[@id="dlPaging_ctl01_lnkbtnPaging"]').click()
#time.sleep(2)
review2= driver.find_element_by_id("dListItems_ctl00_lblFullName")
print("\n\n\nPage-2\n")
print(review2.text)

driver.find_element_by_xpath('//*[@id="dlPaging_ctl02_lnkbtnPaging"]').click()
#time.sleep(2)
review3= driver.find_element_by_id("dListItems_ctl00_lblFullName")
print("\n\n\nPage-3\n")
print(review3.text)

