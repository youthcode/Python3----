import pymongo

print("="*100)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["students"]

result = collection.delete_one({"name": "Jordan"})
print(result)
print(result.deleted_count)

# condition = {"age": {"$gt": 20}}
# result = collection.update_one(condition, {"$inc": {"age": 1}})
# print(result)
# print(result.matched_count, result.modified_count)


# condition = {"name": "Jordan"}
# student = collection.find_one(condition)
# student["age"] = 25
# result = collection.update_one(condition, {"$set": student})
# print(result)







# results = collection.find().sort("name", pymongo.ASCENDING)
# for result in results:
#     print(result)

# results = collection.find().sort("_id", pymongo.ASCENDING).skip(2).limit(2)
# for result in results:
#     print(result["name"])




# count = collection.count_documents({"age": {"$gt": 20}})
# print(count)


# results = collection.find({"name": {"$regex": "^J.*"}})
# print(results)
# for result in results:
#     print(result)

# import pymongo

# print("="*100)

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["test"]
# collection = db.students

# student1 = {
#     "id": "20170101",
#     "name": "Jordan",
#     "age": 20,
#     "gender": "male"
# }

# student2 = {
#     "id": "20170102",
#     "name": "Mike",
#     "age": 21,
#     "gender": "male"
# }

# result = collection.insert_many([student1, student2])
# print(result)

# print("="*100)

# result = collection.find_one({"name": "Jordan"})
# print(type(result))
# print(result)




