# Web Chat app

### Technology used
* **Flask** - used for server side
* **Socket.IO** - used for one-to-one connections

## Project files
Program consists of 7 files

### Python files
* **app.py** - init Flask and Socket.IO variable
* **main.py** - set socket namespace and start server
* **models.py** - describes login form class
* **views.py** - render html templates for site and describes socket class

### HTML files
* **base.html** - used as a site template, contains a navigation bar, socket variable and socket disconnect function
* **index.html** - extends *base.html*, contains login form
* **chat.html** - extends *base.html*, contains chat form and JS function  

## How it works

After the server starts, the chat room login window opens, the **index** function is used for this.
After entering data, the same function enters data into the session and redirects to *'/chat'*. 
The **chat** function reads data from the session and render template with data. 
After the document has been loaded, the socket is connecting to the server(site) 
and JS functions are loaded for working with Socket.IO.
<br>
* **socket.on('Event')** - responsible for sockets event actions 
    * *connect* - alerts that the user has been connected
    * *message* - display user message
    * *options* - display option message as 'connect' or 'disconnect'
    * *disconnect* - alerts that the user has been disconnected

* **send_message** - reads text from *textarea* and add a new message at the end
* **disconnect** - check user connection and leave room if user connected 
(use *Send* button or *Enter* key for send message)

## How to use

1. Run main.py on your computer.
The server will be running at 'http://localhost:5000'.
After starting the server go to the address and you will see this window.
![](media/login.png)

2. Enter username and room to connect to chat.
![](media/chat.png)

3. Open new tab with same address (http://localhost:5000)
and enter the name of the second user and the name of the room.
**The name of the room must match the name of the room of the first user for communication.**
![](media/second_user.png)

4. Now you can send and read messages.
![](media/send_messages.png)

5. After someone leaves the chat, all its participants will be notified. 
If this was done through the "Leave this room" button, then disconnection will occur instantly.
![](media/second_user_left.png)