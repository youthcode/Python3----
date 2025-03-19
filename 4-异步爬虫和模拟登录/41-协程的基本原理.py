import asyncio
import aiohttp
import time

def test(number):
    start = time.time()
    
    async def get(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                return html
            
    async def request():
        url = 'https://www.baidu.com'
        await get(url)
        
    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    
    end = time.time()
    print('Cost time:', end - start)
    
for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)
                
                




# import asyncio
# import aiohttp
# import time

# print('='*50)

# start = time.time()

# # async def get(url):
# #     session = aiohttp.ClientSession()
# #     response = await session.get(url)
# #     await response.text()
# #     await session.close()
# #     return response

# async def get(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             html = await response.text()
#             return html

# async def request():
#     url = 'https://httpbin.org/delay/5'
#     print('Waiting for', url)
#     response = await get(url)
#     print('Get response from', url, 'response', response)

# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# end = time.time()
# print('Cost time:', end - start)








# import asyncio
# import requests

# print('='*50)

# async def request():
#     url = 'https://www.baidu.com'
#     status = requests.get(url)
#     return status

# task = [asyncio.ensure_future(request()) for _ in range(5)]
# print('Tasks:', task)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task))

# for task in task:
#     print('Task Result:', task.result())








# import asyncio
# import requests

# async def request():
#     url = 'https://www.baidu.com'
#     status = requests.get(url)
#     return status

# def callback(task):
#     print('Status:', task.result())
    
# async def main():
#     coroutine = request()
#     task = asyncio.create_task(coroutine)
#     task.add_done_callback(callback)
#     await task

# if __name__ == '__main__':
#     asyncio.run(main())







# import asyncio

# async def execute(x):
#     print('Number:', x)
#     return x

# async def main():
#     coroutine = execute(1)
#     print('Coroutine:', coroutine)
#     task = asyncio.create_task(coroutine)
#     print('Task:', task)
#     await task
#     print('Task:', task)

# asyncio.run(main())









# import asyncio

# async def execute(x):
#     print('Number:', x)
#     return x

# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')

# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task:', task)

# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')





# import asyncio

# print('='*50)

# async def execute(x):
#     print('Number:', x)

# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('After calling loop')














# import requests
# import logging
# import time

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# TOTAL_NUMBER = 10
# URL = 'https://httpbin.org/delay/5'

# start_time = time.time()
# for _ in range(1, TOTAL_NUMBER + 1):
#     logging.info('scraping %s...', URL)
#     response = requests.get(URL)
# end_time = time.time()
# logging.info('total time: %s', end_time - start_time)