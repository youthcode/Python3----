# import pika
# import requests
# import pickle

# MAX_PRIORITY = 100
# TOTAL = 100
# QUEUE_NAME = 'scrape_queue'

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# # 尝试删除已存在的队列（如果存在）
# # try:
# #     channel.queue_delete(queue=QUEUE_NAME)
# #     print(f"已删除现有队列: {QUEUE_NAME}")
# # except Exception as e:
# #     print(f"队列不存在或删除失败: {e}")

# # 重新声明队列
# channel.queue_declare(queue=QUEUE_NAME, durable=True)
# print(f"已创建队列: {QUEUE_NAME}")

# for i in range(1, TOTAL + 1):
#     url = f'https://ssr1.scrape.center/detail/{i}'
#     request = requests.Request('GET', url)
#     channel.basic_publish(exchange='', 
#                           routing_key=QUEUE_NAME, 
#                           properties=pika.BasicProperties(
#                               delivery_mode=2,
#                           ),
#                           body=pickle.dumps(request))
#     print(f'已发送请求: {url}')





import pika
import pickle
import requests

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
session = requests.Session()

def scrape(request):
    try:
        response = session.send(request.prepare())
        print(f'success scrape {request.url}')
    except requests.RequestException:
        print(f'error occurred while scraping {request.url}')
        
while True:
    method_frame, header_frame, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
    if body:
        request = pickle.loads(body)
        print(f'GET {request}')
        scrape(request)



# import pika

# QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# channel.queue_declare(queue=QUEUE_NAME)

# channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body='Hello World!')
# print(" [x] Sent 'Hello World!'")

# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)

# channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()

# connection.close()