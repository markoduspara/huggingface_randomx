
#import pyrx
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	rez=pyrx.get_rx_hash('1','1','1')
	return "Hello World!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
