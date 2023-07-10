from flask import Flask
from flask_pymongo import Pymongo
from bson.objectid import ObjectId
app=Flask(__name__)
app.config["Mongo_URL"]="mangodb://localhost:270017/kaka"
mango=Pymongo(app)
data_collection=mango.db.data
@app.route("/",methods=["GET"])
def getdata():
    datas=data_collection.find()
    data1=[]
    for data in datas:
        data["-id"]=str(data["_id"])

@app.route("/add",methods=["POST"])
def adddata():   
@app.route("/uddate/<id>",methods=["PUT"])
def adddata():  
@app.route("/delete/<id>",methods=["DELETE"])
def adddata():         
if_name=="_main":
app.run()