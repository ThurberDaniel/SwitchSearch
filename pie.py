from flask import Flask# Import Flask to allow us to create our app
app = Flask(__name__) 

 
@app.route('/test')
def hello_test():
    return 'test'
 ***************************************************************
 *******************************

@app.route('/<name>')
def hello_name(name):
    print(name)
    return f" Hello {name}"

@app.route('/repeat/<int:number>/<name>')
def number(number,name):
    print(name)
    print(number)
    return f"{name}"*number


@app.route('/say/<name>')
def hello_world(name):
    return f'Say {name}'



if __name__=="__main__":
    app.run(debug=True)