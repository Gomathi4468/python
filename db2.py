import pymongo
con=pymongo.MongoClient("mongodb+srv://kavitha:Kavitha1999@cluster0.ueov9pz.mongodb.net/?retryWrites=true&w=majority")
print("connection sucessfully")
mydb = con["mydatabase"]
mycol = mydb["customers"]
mydict={"name":"vijay","age":30}
x=mycol.insert_one(mydict)
print("collect")

