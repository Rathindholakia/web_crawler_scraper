
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

fd = open("contacts","w+")
writer = csv.writer(fd)
writer.writerow(['Name','Designation','ResAddress','Contact','Email'])

chrome_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)

pages=[14]

#======= Open Site =========
driver.get("http://www.associationofchemistryteachers.org/MembersDirectories.aspx")

#------ Go to Alphabet ----------
driver.find_element_by_xpath('//*[@id="lbtnA"]').click()
for j in range(0,pages[0]):
    if j != 0:
        page_id = '//*[@id="dlPaging_ctl%02d_lnkbtnPaging"]'%(j)
        driver.find_element_by_xpath(page_id).click()
        
    for i in range(0,12):
        entry = [] 
        name_id =   "dListItems_ctl%02d_lblFullName"%(i)
        desg_id =   "dListItems_ctl%02d_lblDesignation"%(i)
        resAdd_id = "dListItems_ctl%02d_lblResAddress"%(i)
        con_id =    "dListItems_ctl%02d_lblContact"%(i)
        email_id =  "dListItems_ctl%02d_lblEmail"%(i)
        
        try:
            name= driver.find_element_by_id(name_id)
            print(name.text)
            entry.append(name.text)
        except:
            break
        

        desg= driver.find_element_by_id(desg_id)
        print(desg.text)
        entry.append(desg.text)

        resAdd= driver.find_element_by_id(resAdd_id)
        print(resAdd.text)
        entry.append(resAdd.text)

        con= driver.find_element_by_id(con_id)
        conE = con.text[9:]                         #Strip out field name "Contact: ""
        print(conE)
        entry.append(conE)

        email= driver.find_element_by_id(email_id)
        emailE = email.text[7:]                     #stip out "email: field name"              
        print(emailE)
        entry.append(emailE)

        print(entry)

        #---Write to file----
        writer.writerow(entry)

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


