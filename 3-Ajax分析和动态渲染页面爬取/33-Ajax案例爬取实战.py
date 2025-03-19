import requests
import logging
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)
    return None  # 明确返回None，以便后续处理

LIMIT = 10

def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'

def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

TOTAL_PAGE = 10

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'

client = MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)

def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        if not index_data:
            logging.error('获取第 %s 页数据失败', page)
            continue
        
        results = index_data.get('results')
        if not results:
            logging.error('第 %s 页没有results数据', page)
            continue
            
        logging.info('获取第 %s 页数据成功，共 %s 条数据', page, len(results))
        for item in results:
            id = item.get('id')
            if id:
                detail_data = scrape_detail(id)
                logging.info('detail data %s', detail_data)
                save_data(detail_data)
                logging.info('数据已保存到MongoDB')
            else:
                logging.warning('没有找到id字段')

if __name__ == '__main__':
    main()

# print('='*50)

# import requests

# url = 'https://spa1.scrape.center/'
# html = requests.get(url).text
# print(html)
