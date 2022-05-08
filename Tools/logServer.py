from typing import List
from flask import make_response
from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify

MSG_POOL=list()
# max message numbers in pool 
POOL_SIZE=10

# message pool cache
def flushMsgPool(msg):
    if len(MSG_POOL)<POOL_SIZE:
        MSG_POOL.append(msg)
    else:
        MSG_POOL.remove(MSG_POOL[0])
        MSG_POOL.append(msg)


app = Flask(__name__)
# ensure send utf-8 characters
app.config["JSON_AS_ASCII"]=False 

# POST method, receive a message from logger and push into message pool
@app.route("/send",methods=['POST'])
def send():
    try:
        MSG=dict()
        MSG['msg']=request.form["msg"]
        print(MSG)
        flushMsgPool(msg=MSG)
        return jsonify({'result': MSG_POOL})
    except:
        return jsonify({'result': MSG_POOL})

# GET method, return message poll's messages
@app.route("/get",methods=['GET'])
def getMsg():
    return jsonify({'result': MSG_POOL})


# start server engine
if __name__=='__main__':
    app.run(host="0.0.0.0",port=1140)