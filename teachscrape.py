
########################################################
#       Web Scraper
#       Date: 22-June-2019
#       Name: Rathin Dholakia
#       ToDO :  1. Create list of item for appending to list
#               2. write to file
#               3. For loop implementation
#               4. Add Number array for # of pages in alphabet
#               5. Add umber of entries per pages-- otherwise script will exit
from selenium import webdriver
import time
import csv

fd = open("contacts","+w")
writer = csv.writer(fd)
writer.writerow['Name','Designation','ResAddress','Contact','Email']

chrome_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)

#======= Open Site =========
driver.get("http://www.associationofchemistryteachers.org/MembersDirectories.aspx")
contact =[] 

#------ Go to Alphabet ----------
driver.find_element_by_xpath('//*[@id="lbtnA"]').click()
name_id = "dListItems_ctl%02d_lblFullName"%(00)
name= driver.find_element_by_id(name_id)
print(name.text)
contact.append(name.text)
desig= driver.find_element_by_id("dListItems_ctl00_lblDesignation")
print(desig.text)
contact.append(desig.text)
resAdd= driver.find_element_by_id("dListItems_ctl00_lblResAddress")
print(resAdd.text)
con= driver.find_element_by_id("dListItems_ctl00_lblContact")
print(review.text)
review= driver.find_element_by_id("dListItems_ctl00_lblEmail")
#print(type(review))
print(review.text)
#for post in review:
#    print(post.text)
print(contact)

#---Write to file----


#-------- Change Page -----------------
driver.find_element_by_xpath('//*[@id="dlPaging_ctl01_lnkbtnPaging"]').click()
#time.sleep(2)
review2= driver.find_element_by_id("dListItems_ctl00_lblFullName")
print("\n\n\nPage-2\n")
print(review2.text)



#========== Change of Letter ==============================
driver.find_element_by_xpath('//*[@id="lbtnB"]').click()


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


