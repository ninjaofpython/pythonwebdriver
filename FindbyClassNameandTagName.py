from selenium import webdriver
import os
import time

class FindByClassNameandTagName():
   
    
    def test(self):
        baseURL = "https://www.python.com"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing find the element.")

        if elementByClassName is not None:
            print("We found an element by ClassName")

        elementByTagName = driver.find_element_by_tag_name("h1")
        elementByTagName.send_keys("Testing this with tag_name element.")
        if elementByTagName is not None:
            print("We found the element by Tag Element!")
ff = FindByClassNameandTagName()
ff.test()
