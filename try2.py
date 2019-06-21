from selenium import webdriver
chrome_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)


driver.get("https://www.sephora.com/product/double-wear-stay-in-place-makeup-P378284?icid2=recommended%20for%20you:p378284:product")

review= driver.find_element_by_class_name("css-1p4f59m ")
print(review.text)
#print(review)
#for post in review:
#    print(post.text)

