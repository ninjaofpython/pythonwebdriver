from selenium import webdriver
import os
import time

class FindByClassNameandTagName():
   
    
    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing this thing 1")

        if elementByClassName is not None:
            print("We found an element by ClassName")

        elementByTagName = driver.find_element_by_tag_name("h1")
        elementByTagName.send_keys("Testing this thing")
        if elementByTagName is not None:
            print("We found the element by Tag Element!")
ff = FindByClassNameandTagName()
ff.test()
