from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException



import csv
import time

def get_grade(wr, sitter_id):
    driver.get('https://www.mom-sitter.com/detail/sitter/'+str(sitter_id)+'/reviews?tab=recruitReview')
    grade_count = 1
    while True:
        try:
            text = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[3]').text.replace('\n', '')
        except UnexpectedAlertPresentException:
            text = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[3]').text.replace('\n', '')
        
        except:
            break

        star_count = 0
        for i in range(1, 6):
            star = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[2]/div[1]/img['+str(i)+']').get_attribute('src')
            if 'star_on' in star:
                star_count+=1
            
        wr.writerow([sitter_id, star_count, text, 1])
        grade_count += 1

    grade_count = 1
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/p').click()
    while True:
        try:
            text = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[3]').text.replace('\n', '')
        except UnexpectedAlertPresentException:
            text = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[3]').text.replace('\n', '')
        
        except:
            break

        star_count = 0
        for i in range(1, 6):
            star = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[2]/div[1]/img['+str(i)+']').get_attribute('src')
            if 'star_on' in star:
                star_count+=1            
        wr.writerow([sitter_id, star_count, text, 2])
        grade_count += 1

    grade_count = 1
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]').click()
    while True:
        try:
            text = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[3]').text.replace('\n', '')
        except UnexpectedAlertPresentException:
            text = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[3]').text.replace('\n', '')
        
        except:
            break

        star_count = 0
        for i in range(1, 6):
            star = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div['+str(grade_count)+']/div[1]/div[1]/div[2]/div[2]/div[1]/img['+str(i)+']').get_attribute('src')
            if 'star_on' in star:
                star_count+=1
        wr.writerow([sitter_id, star_count, text, 3])
        grade_count += 1


driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(5)
driver.get("https://www.mom-sitter.com/")
da = Alert(driver)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/button[2]/div/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[1]/input[1]').send_keys('jjo3ys')
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[1]/input[2]').send_keys('dustjd273')
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/button').click()

time.sleep(1)
try:
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/button[1]/div/span').click()
except UnexpectedAlertPresentException:
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/button[1]/div/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/button').click()

with open("sitter_data.csv", 'w', encoding='utf-8', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['시터id'])
    sitter_count = 1
    for i in range(1, 4):
        try:
            count = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div['+str(i)+']/div/div[2]/div[2]/div[4]/div/span').text
        except:
            count = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div['+str(i)+']/div/div[2]/div[2]/div[4]/div/span').text

        count = count.lstrip('후기 ')
        count = count.rstrip('개')
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div['+str(i)+']/div').click()
        sitter_id = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]').text.lstrip('no.')
        wr.writerow([sitter_id])

        driver.get('https://www.mom-sitter.com/search/sitter')
        time.sleep(1)

    try:
        count = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[4]/div[2]/div[2]/div[2]/div[4]/div[1]/span').text
    except:
        count = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[4]/div[2]/div[2]/div[2]/div[4]/div[1]/span').text
    count = count.lstrip('후기 ')
    count = count.rstrip('개')
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[4]/div[2]/div[2]').click()
    sitter_id = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]').text.lstrip('no.')
    wr.writerow([sitter_id])

    driver.get('https://www.mom-sitter.com/search/sitter')
    time.sleep(1)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[4]')).perform()
    time.sleep(1)


    while True:  
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight+300)")
        try:
            count = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[5]/div/div[2]/div[2]/div[4]/div/span').text
            print(count)
                                                
        except NoSuchElementException:                                           
            try:
                count = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[5]/div/div[2]/div[2]/div[4]/div[1]/span').text
            except NoSuchElementException:
                count = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[5]/div/div[2]/div[2]/div[4]/div/span').text
        
    
        count = count.lstrip('후기 ')
        count = count.rstrip('개')
        if int(count) == 0:
            break
        
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[5]/div/div/div[2]').click()
        sitter_id = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]').text.lstrip('no.')
        wr.writerow([sitter_id])

        driver.back()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight+300)")
        
        time.sleep(3)