Objective: Facilitates direct communication between clients via a central server.

Server: Orchestrates connections among clients, relaying messages from one client to another.

Features:

* Establishes a TCP Socket.
* Listens for incoming connections.
* Upon a new client's connection, the server accepts it and adds the client to a client dictionary. Each entry consists of the client's socket object as the key and its address as the value.
* Initiates a new thread to manage client messages using the handle_client() method.
* This method continuously listens for messages from the client.
* If the message is a keep-alive signal, the server maintains the connection.
* If the message requests a list of clients, the server provides the client dictionary's contents.
* For chat messages, the server forwards them to all clients except the sender and logs them in an SQLite database.
* Error handling: If a message receiving error occurs, the server removes the client from the dictionary and closes its socket.
* Client: Connects to the server to engage in chats with other clients by sending messages through the server.

Features:

* Establishes a TCP socket.
* Connects to the server.
* Enters a loop prompting the user for messages.
* If the message is "list," the server provides a list of connected clients.
* If the message is "chat," the client prompts for the recipient's IP address and message text.
* The client sends the chat message to the server.
* It sends a keep-alive message every 30 seconds to prevent connection closure due to inactivity.
* The client waits up to 5 seconds for a server response, displaying it on the console if received.