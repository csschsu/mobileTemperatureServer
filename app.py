from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/temperatur',methods=['GET','POST'])
def hello_temp():

    if request.method == 'POST':

        filedata = str(request.json)
        filedata = filedata.replace('\'','\"')
        print (filedata)
        f = open('temperatur.json', 'w')
        f.write(filedata)
        f.close()
        return jsonify(isError= False,
                       message= "Success",
                       statusCode= 200)
    else :
        f = open('temperatur.json', 'r')
        data = f.readline()
        f.close()
        print( data)
        payload=json.loads(data)
        return jsonify(payload)



if __name__ == '__main__':
    app.run(port=5000)
