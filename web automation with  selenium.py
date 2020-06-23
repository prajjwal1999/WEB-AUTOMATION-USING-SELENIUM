#!/usr/bin/env python
# coding: utf-8

# In[ ]:




from selenium import webdriver


browser=webdriver.Chrome()



browser.get("https://www.codechef.com")





username=browser.find_element_by_id("edit-name")


print("Enter Usrname ")
usr=input()

username.send_keys(usr)


password=browser.find_element_by_id("edit-pass")



print("Enter password")
passwrd=input()



password.send_keys(passwrd)


browser.find_element_by_id("edit-submit").click()



print("Enter the problem code to be submitted")
pcode=input()




browser.get("https://www.codechef.com/submit/"+pcode)



browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


with open("main.cpp") as f:
    code=f.read()



code_ele=browser.find_element_by_id('edit-program')


code_ele.send_keys(code)


browser.find_element_by_id("edit-submit-1").click()



