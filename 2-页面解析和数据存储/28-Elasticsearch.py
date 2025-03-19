print('=' * 100)

# from elasticsearch import Elasticsearch

# # 指定hosts参数，连接到本地Elasticsearch
# es = Elasticsearch(hosts=["http://localhost:9200"])
# es = es.options(ignore_status=400)
# result = es.indices.create(index='news')
# print(result)


# 删除 news 索引
# from elasticsearch import Elasticsearch

# es = Elasticsearch(hosts=["http://localhost:9200"])
# result = es.indices.delete(index='news', ignore=[400, 404])
# print(result)

# 插入数据
# from elasticsearch import Elasticsearch

# es = Elasticsearch(hosts=["http://localhost:9200"])
# # es.indices.create(index='news', ignore=400)
# es.options(ignore_status=[400]).indices.create(index='news')

# data = {
#     'title': 'Python 3.20 正式发布',
#     'url': 'https://www.python.org/downloads/release/python-3100/',
#     'date': '2021-10-04'
# }

# # 确保文档存在后再更新
# es.index(index='news', id=2, document=data, op_type='create', ignore=409)
# # 使用正确的update格式
# result = es.update(index='news', id=2, body={'doc': data})
# print(result)

# 删除数据 id =1
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=["http://localhost:9200"])
result = es.delete(index='news', id=1)
print(result)
