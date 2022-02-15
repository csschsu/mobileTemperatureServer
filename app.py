# Mapping json to memory
# Prometheus push concept for external device with mobilebroadband
# connection with no pull possibility
# Data is available as long as this service runs
# curl -X POST http://localhost:5000/temperature -H "Content-Type: application/json" -d '{"counter": 1234, "values":[ {"id": "1", "temp": 11.75}, {"id": "2", "temp": 35.31}, {"id": "3", "temp": 38.69}], "location": "PI-2"}'

from flask import Flask, jsonify, request
import memory

app = Flask(__name__)

@app.route('/temperature', methods=['GET', 'POST'])
def hello_temp(cache=None):
    print(md.mem)
    if request.method == 'POST':

        md.mem = request.json
        print (md.mem)
        return jsonify(isError= False,
                       message= "Success",
                       statusCode= 200)
    else:
        print(md.mem)
        return md.mem


if __name__ == '__main__':
    md = memory.Memory({'initial': 0})
    app.run(port=5000)
