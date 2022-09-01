from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://localhost:27017/')
filter={}

result = client['Rough']['myData'].find(
  filter=filter
)
print(*result)