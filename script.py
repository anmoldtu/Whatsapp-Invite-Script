import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd
df = pd.read_excel(io='Responses.xlsx')
print(df.head(5))
message = "Hey " + df['Name'][0] + ",Please Join the following group  "
print(message)
driver = webdriver.Chrome('../Downloads/chromedriver_3')
x = ""
start = 0;
for i in range(start,df.shape[0]):
    number = df['Phone Number']
    if(number[i] != "+") :
        number = "+91" + str(number[i])
    url = "https://api.whatsapp.com/send?phone=" + number
    print(url)
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="action-button"]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
    driver.implicitly_wait(20)
    operator = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    if(df['Response'][i] == "Yes") :
        x = message + "https://chat.whatsapp.com/CuQHP3Dy1sd3WA0nq3gaCu"
    else :
        x = message + 'link2'
    operator.send_keys(x)
    operator.send_keys(Keys.ENTER)
    time.sleep(5)