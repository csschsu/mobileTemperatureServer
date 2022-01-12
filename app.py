from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/temperatur',methods=['GET','POST'])
def hello_temp():


    if request.method == 'POST':
        temperatur = request.json.get('temperatur')
        password = request.json.get('password')
        data = "{ 'temperatur': '" + temperatur + "' }\n"
        f = open('config.json', 'w')
        f.write(data)
        f.close()
        return jsonify(isError= False,
                       message= "Success",
                       statusCode= 200,
                       data= data)
    else :
        f = open('config.json', 'r')
        data = f.readline()
        f.close()
        return data

# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('temperatur')
        framework = request.form.get('grader')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

if __name__ == '__main__':
    app.run(port=5000)
