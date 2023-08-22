'''We are creating a small program for API(Appliaction Programming Interface)\n 
For creating an API we will use flask library. Flask is an in built library in python which is used for creating APIs\n 
We will be using client and server based architecture that we studied earlier.\n
So lets start by importing 'Flask' function from 'flask' library.''' 

from flask import Flask

# Now we will create an object of Flask function(i.e. class) using dunder method and also we will assign a varibale to it.
app = Flask(__name__)
# Here we can see we use 'app' as variable name. Now this variable will inherit everything that is is the flask class.

#Now we will create any desired function. We will use a decorator (i.e. 'app.route("/")') with the function.
#We know we are creating a client server architecture of API in which client can access anything in a server through a route.
#So this python code here is the server and the client will be any browser through which server's address is accessed and this decorator here 'app.route("/")' is the route which enables the client to access functions that are created in the server.
#The ("/") is used after client enters full address of the server to access the respective function. Let see:

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# Here <h1> is the head tag of html used to define size of the string h1 means largest then h2, h3, h4 are in decreasing order
# We can also use other function with different routes such as:

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"

@app.route("/test")
def test():
    a = 5+6
    return "<h1>This is my function to run app %d</h1>" %(a)

# We can also request the client to enter some value. This value can be a string or an integer.
# So for this we will import request function from flask library.
# We are using 'request.args.get('x')' and then assign it to a variable 'data'. This function will require the client to enter some input.

from flask import request

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "<h3>this is a data input from my url %s </h3>" %(data)

# The user will enter the data after entering complete address including url, port number and route. After route a question mark is used followed by x = user input.
# It will look like this: (url:5000/test2? x = tabish)

# Finally we will run the app variable in "__main__" function and will set local host to "0.0.0.0"

if __name__=="__main__":
    app.run(host="0.0.0.0")

# Now to access this server first client needs to reach the machine (i.e. place where server is running).
# So for that we need to copy url of this lab (till app). This url is the way to reach the server.
# Now paste this url in the browser and enter port number as 5000 (i.e. url:port_number).
# As soon as we enter the url we will see output of first function as its route is ("/") only.
# We can use this url to access this server from anywhere like mobile or laptop etc.
# To access other function we use '/' followed by route of that function for example if we have to access second function i.e. hello_world1, we will enter url followed by port number and then we will give slash and enter the route of second function i.e. url:5000/hello_world1