from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print('正在启动浏览器...')
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    def modify_response(route,response):
        route.fulfill(path='custom_response.html')
        
    page.route('**/*', modify_response)
    
    print('正在访问页面...')
    page.goto('https://spa6.scrape.center/')
    page.wait_for_timeout(3000)
    print('完成！')
    browser.close()





# from playwright.sync_api import sync_playwright
# import re

# def cancel_request(route):
#     route.abort()

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     page.screenshot(path='no_picture.png')
#     browser.close()

    




# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     elements = page.query_selector_all('a.name')
#     for element in elements:
#         href = element.get_attribute('href')
#         title = element.text_content()
#         print(href, title)
#     browser.close()




# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     html = page.content()
#     print(html)
#     browser.close()






# from playwright.sync_api import sync_playwright

# def on_response(response):
#     # print(f'Status {response.status}: {response.url}')
#     if '/api/movie' in response.url and response.status == 200:
#         print(response.json())
    
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.on('response', on_response)
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     browser.close()





# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     iphone_12_pro_max = p.devices['iPhone 12 Pro Max']
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context(
#         **iphone_12_pro_max,
#         locale='zh-CN',
#         geolocation={'longitude': 116.39014, 'latitude': 39.913904},
#         permissions=['geolocation']
#         # user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#     )
#     page = context.new_page()
#     page.goto('https://amap.com')

#     # page.wait_for_load_state(state='networkidle')
#     # page.goto('https://spa2.scrape.center/')  # 你也可以换成 antispider1.scrape.center
#     page.wait_for_load_state(state='domcontentloaded')  # 只等待 DOM 加载即可，不必等网络稳定
#     page.wait_for_timeout(5000)  # 明确等待 5 秒钟，确保页面加载完全
    
#     page.screenshot(path='location-iphone.png')
#     browser.close()

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     iphone_12_pro_max = p.devices['iPhone 12 Pro Max']
#     browser = p.chromium.launch(headless=False)  # 换为chromium内核尝试
#     context = browser.new_context(
#         **iphone_12_pro_max,
#         locale='zh-CN',
#         geolocation={'longitude': 116.39014, 'latitude': 39.913904},
#         permissions=['geolocation']
#     )

#     page = context.new_page()
#     page.goto('https://antispider1.scrape.center/')
#     page.wait_for_timeout(2000)  # 等待2秒，确保页面内容完全加载

#     # 可选操作，例如截屏查看结果
#     page.screenshot(path='test_result.png')

#     browser.close()


# import asyncio
# from playwright.async_api import async_playwright


# async def main():
#     async with async_playwright() as p:
#         for browser_type in [p.chromium, p.firefox, p.webkit]:
#             browser = await browser_type.launch()
#             page = await browser.new_page()
#             await page.goto('https://www.baidu.com')
#             await page.screenshot(path=f'screenshot-{browser_type.name}.png')
#             await browser.close()

# asyncio.run(main())

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch(headless=False)
#         page = browser.new_page()
#         page.goto('https://www.baidu.com')
#         page.screenshot(path=f'screenshot-{browser_type.name}.png')
#         print(page.title())
#         browser.close()
