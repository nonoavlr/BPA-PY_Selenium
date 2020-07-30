# Import Selenium to manipulate DOM and Pandas to generate xlsx
from time import sleep
from selenium import webdriver
import pandas as pd

# GO TO https://chromedriver.chromium.org/
# Confirm you google chrome version and download the driver
# Open the driver with WebDriver to open a window
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Get the link to manipulate DOM
driver.get('https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2')

# CF = Complete root
# driver.get('https://www.amazon.com.br/')

#Set the lists
titles = []
prices = []

#CF
# textsearch = "iphone"
# sleep(2)
# fase1 = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(textsearch)
# sleep(4)
# fase2 = driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]/input').click()
# sleep(2)

#The page show us 24 items. The max range should be len(items) + 1
for i in range(1,25):
    #Using interpolation to select automatically each xpath root and convert to text
    title = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[2]/h2/a/span'
    .format(i = i)).text

    #Add to list title
    titles.append(title)

    #I tried too many forms to select the full price but I just catch only by this way
    #First try/exception by XPATH whole-price
    try :
        price = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[4]/div/div/a/span/span[2]/span[2]'
        .format(i = i)).text.replace('.','') + '.'
    except:
        price = '0.'

    #Second try/exception by XPATH price-fraction
    try :
        subprice = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[4]/div/div/a/span/span[2]/span[3]'
        .format(i = i)).text
    except:
        subprice = '0'

    #Add the float convertion 
    prices.append(float(price + subprice))



#Inicialize panda strcture data
df = pd.DataFrame()

#Set the name columms with the values
df['Titles'] = titles
df['Prices'] = prices

#Export to excel
df.to_excel('./iphone_search.xlsx', index = False)

#Close the window
driver.quit()