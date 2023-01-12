import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Rares:Negrut@cluster0.lwhghcy.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["sample_training"]
mycol = mydb["grades"]

myquery = { "student_id": 0 }

print(myclient.get_database("sample_training"))

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x) 