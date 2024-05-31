# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:55:08 2024

@author: user
"""

from selenium import webdriver
from selenium.webdriver.common.by import By  # Importing By class from selenium.webdriver.common.by
import time
import pandas as pd


class Downloader():
    def __init__(self,url):
        self.url =url
    
    def extraction():
        url = 'https://syarah.com/en/filters?page=2'
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)
        
        # Creating an empty dictionary
        filter_name=[]
        filter_values =[]
        lis=['Year','Price','Odometer']
        
        all_div = driver.find_elements(By.CLASS_NAME,'AsideBody-module__wrapper ')
        
        for div in all_div:
            a=div.find_element(By.CLASS_NAME,'OpenMenuSelection-module__container  ').text
            
            b = driver.find_elements(By.CLASS_NAME,'SubFilterOpenButton-module__container  ')
        filter_name.append(a.split('\n')[0])
        value = a.split('\n')[1]+' '+a.split('\n')[2]
        filter_values.append(value)
        
        time.sleep(1)
        
        for b1 in b:
            time.sleep(1)
            # Click on filter name
            if b1.text in lis:
                print('Skip')
                pass
        
            else:
                try:
                    b1.click()
                except:
                    print('inside except')
                    time.sleep(4)
                    b1.click()
                time.sleep(1)
                # Get filter name
                n = driver.find_element(By.CLASS_NAME,'SubMenuContainer-module__headingPart').text
                filter_name.append(n)
                
                # Get all values of filters
                Q = driver.find_elements(By.CLASS_NAME,'CheckBox-module__container') 
                value = ''
                for q in Q:
                    # Input-module__inputWrapper Input-module__targeted    
                    print(q.text)
                    value = value+' '+q.text
                # if value == ' Used New':
                #     print('yes')
                #     driver.find_element(By.NAME,'min').get_attribute('value')
                filter_values.append(value)
                # filter_name.append(b1.text)
                # Return back to page
                driver.find_element(By.CLASS_NAME,'SubMenuContainer-module__headingPart').click()
                time.sleep(2)
                
        filter_values = [i.strip() for i in filter_values] 
        filter_values = jo
        filter_values = [i.replace('Used New','',1) for i in filter_values]
        filter_name = [i for i in filter_name if i != 'Shape']
        filter_values[11] = 'Used New'
        filter_values = filter_values.remove('')
        
        # Create a dictionary using dictionary comprehension and zip()
        filter_dict = {k: v for k, v in zip(filter_name, filter_values)}
        # Create DataFrame from dictionary
        df = pd.DataFrame([filter_dict],index=[0])
        df.to_csv('Extracted_Filters.csv',index=False)
        
        