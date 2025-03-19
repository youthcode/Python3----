
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.set_window_size('1920', '1080')
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('preview.png')


# from selenium import webdriver
# from selenium.webdriver import ChromeOptions

# options = ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('useAutomationExtension', False)
# browser = webdriver.Chrome(options=options)
# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
# })

# browser.get('https://antispider1.scrape.center/')


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# print('='*50)
# browser = webdriver.Chrome()
# try:
#     # browser.get('https://www.baidu.com')
#     browser.get('https://antispider1.scrape.center/')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element(By.ID, 'hello')
# except NoSuchElementException:
#     print('No Element Found')
# finally:
    # browser.close()






# import time
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://www.python.org')
# browser.close()



# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print('='*50)
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print('='*50)
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print('='*50)
# print(browser.get_cookies())
# browser.close()







# import time
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)







# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://spa2.scrape.center/')
# input = browser.find_element(By.CLASS_NAME, 'logo-image')
# print(input)
# browser.close()



# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element(By.CLASS_NAME, 'logo')
#     print(logo)
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element(By.CLASS_NAME, 'logo')
# print(logo)
# print(logo.text)
# browser.close()





# from selenium import webdriver
# from selenium.webdriver.common.by import By

# print('='*50)

# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# # logo = browser.find_element(By.CLASS_NAME, 'logo-image')
# # print(logo)
# # print(logo.get_attribute('src'))

# input = browser.find_element(By.CLASS_NAME, 'logo-title')
# print(input.text)
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# browser.close()










# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')










# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element(By.CSS_SELECTOR, '#draggable')
# target = browser.find_element(By.CSS_SELECTOR, '#droppable')
# action = ActionChains(browser)
# action.drag_and_drop(source, target)
# action.perform()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element(By.ID, 'q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element(By.CSS_SELECTOR, '.btn-search')
# button.click()








# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# # lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR, 'a.cate-content-href--HI8wwRts')
# # print(lis)
# for li in lis:
#     print(li.text, end=' ')
# print()  # 最后添加一个换行
# browser.close()










# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# # lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# elements = browser.find_elements(By.CSS_SELECTOR, '.cate-content-href--HI8wwRts')
# for element in elements:
#     print(element.text)
# browser.close()





# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID, 'q')
# input_second = browser.find_element(By.CSS_SELECTOR, '#q')
# input_third = browser.find_element(By.XPATH, '//*[@id="q"]')
# print(input_first, input_second, input_third)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID, 'q')
# input_second = browser.find_element(By.CSS_SELECTOR, '#q')
# input_third = browser.find_element(By.XPATH, '//*[@id="q"]')
# print(input_first, input_second, input_third)
# browser.close()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element(By.ID, 'kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     # print(browser.current_url)
#     # print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# from selenium import webdriver
# from time import sleep

# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# sleep(2)
# browser.close()
