This is a chat programme or platform that enables people to communicate in real time via their desktop or mobile web browsers while the server protects their sensitive information. Users have access to a variety of tools and options that make communicating with their counterparts easy and enjoyable.
It is possible to send pictures, audio files, and text messages with emoji options. In order to keep things interesting, real-time voice or audio calls can also be made.

Features
Light or Dark Theme
To give customers flexibility of choice when it comes to application design, the app now offers a light or dark theme option. This functionality was created with Tailwind CSS.

Chat Pinning
A sorting algorithm was used to enable the chat pinning function, which enables users to store their favourite chat at the top of the chat list for easy access.

Chat Search
A sorting algorithm was used to construct the chat searching tool, which enables users to look for a previous conversation with a contact who may have dropped off the chat list.

New Private Chat
This shortcut link was constructed using Redux dispatch actions to allow users to begin a new chat with someone on their contact list.

Delete Chat
Through the server API and Redux dispatch actions, a delete chat functionality was created to allow users to get rid of old chats they might not be comfortable with or believe are no longer relevant.

User settings
This was accomplished by using Cloudinary to store picture uploads and server API to make changes to user profile details. User settings are enabled to allow users to alter their profile settings, such as uploading a new profile picture, updating their nickname, or submitting a new bio status.

Contact List
Users may browse through all of their contacts and even start a chat with them by clicking on the contact list feature, which was made possible with Redux dispatch actions.

Contact Search
Users can use the contact search tool to look up certain people they want to communicate with. Sorting algorithms enabled this capability.

Add Contact
Users can now create a new contact for someone they recently met or knew by using the Add Contact functionality, which was enabled by using the server API and Redux dispatch actions.

Delete Contact
This functionality was created specifically to address the problem of having an unwanted contact on our contact list using server API and Redux dispatch actions.

Contact Profile
Using Redux dispatch actions and React dynamic rendering, the contact profile checking functionality enables users to check contacts' profiles to zoom in on their profile pictures and view additional information about them.

Contact Online Status
A feature called "Contact online status" allows users to view whether a contact is online right now and whether they were offline when they exited their app. This feature was created utilising Socket.io to transmit online or offline status in real-time and MongoDB to store user online or offline status.

Emojis
The React emoji picker library was used to provide the emoji feature, which enables users to contribute amusing reactions to discussions.

Voice recording
Users can record audio and send it to others using this feature. React media recorder library was used to capture audio from users, and Cloudinary was used to store uploaded audio.

Send Photo
Users may exchange photographs while talking thanks to this functionality, which uses Socket.io to share photos in real time and Cloudinary to store uploaded photos.

Calls
By using Socket.io to deliver call requests to users in real-time and WebRTC to enable real-time media transmission, this feature allows users to make voice or video calls.

Call Records
Users can access this feature to view records of calls they've made and their details. React was used to display the records, and MongoDB was used to store the records.

Chatbot
Users can enjoy themselves on the app with the Telegram Chatbot while some of their connections may be offline thanks to the integration of this functionality. This was made possible by using a Chatbot RESTful API to send messages and get responses from the chatbot.
