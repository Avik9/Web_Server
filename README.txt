# Avik Kadakia
# akadakia
# 111304945
# 
# CSE 310
# PA 1

Things included in the zip file:
    README.txt (This File)
    serverMT.py
    server.py
    client.py
    test.sh
    Screenshots folder
        Single Threaded
        Multi Threaded
	Client Server


Here is how you can test single threaded the server:

Run the server.py file. By default, the server's name will be localhost and the port that it will run on will be 12000. Once the file is ready and "Ready to serve..." is displayed in the console, open a browser and enter "localhost:12000/HelloWorld.html". This should return the contents of HelloWorld.html and the browser would look like the picture labeled as "HelloWorld" in the Single threaded folder under Screenshots. 

Next, you can try searching for a file that does not exist and hence replace the "HelloWorld.html" in the address bar with "HelloWorl.html" or whatever you like. It should look like the picture labeled as "Not Found" in the same folder. 

Additionally, to truly see the sequential run of the server, you can uncomment the 32nd line of the file that reads "time.sleep(2)" and run the test.sh file in the zip file. This would result in the script making 10 requests to the server and they will all arrive at an interval of 2 seconds. You can see this in the screenshot labeled as "script-test" in the same folder.


Here is how you can test the multi threaded server:

The two parts different for the multi threaded server would be to run the "serverMT.py" file and the test run with "test.sh". In order to make this, uncomment line 59 and run the script. This will result in mixed response since multiple thread will return at the same time.

The screenshot for the multi threaded server are provided in the multi threaded folder under the same names. If you look closely in the "script-test" screenshot, you will see that the responses for 2 different requests are mixed up. Hence, proving that the server is multi threaded.


Here is how you can run the client:

You can either run the client by providing any number of arguments after the name of the file. The format for the arguments are as such:
client.py server_host server_port filename

These are the default values that will be used if a value for them has not been provided:
	server_host : localhost
	server_port : 12000
	filename: HelloWorld.html

You can use the client server with the servers and you should receive a valid response. I have attached screenshots of what it returns for the multi threaded server in the Client Server folder for a valid and invalid file name.
