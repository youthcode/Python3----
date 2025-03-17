import json

data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))






# import json

# print('=' * 50)

# with open('data.json', encoding='utf-8') as file:
#     str_data = file.read()
#     data = json.loads(str_data)

# print(data)





# import json

# with open('data.json', encoding='utf-8') as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data)




# import json
# str = '''
# [
#     {
#         "name": "Bob1",
#         "gender": "male",
#         "birthday": "1990-01-01"
#     }
# ]
# '''
# data = json.loads(str)
# print(data)



# import json

# str = '''
# [
#     {
#         "name": "Bob1",
#         "gender": "male",
#         "birthday": "1990-01-01"
#     },
#     {
#         "name": "Selina2",
#         "gender": "female",
#         "birthday": "1991-02-02"
#     }
# ]
# '''
# # print(type(str))
# data = json.loads(str)
# # print(data)
# # print(type(data))

# print(data[0]['name'])





