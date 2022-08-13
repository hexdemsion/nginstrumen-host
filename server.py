from flask import Flask, request

app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hello from host server"



@app.route('/receive-file', methods=['POST'])
def receive_file():
    if request.method == 'POST':
        f = request.files['fileku']
        f.save(f.filename)
        return 'file uploaded successfully'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)

