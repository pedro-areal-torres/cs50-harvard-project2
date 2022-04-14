# PROJECT 2 - Pedro Torres

## Presentacion Video
https://youtu.be/COODLj45iEQ

## Overview
In this project, I built an online messaging service using Flask, similar in spirit to Slack. Users will be able to sign into your site with a display name, create channels (i.e. chatrooms) to communicate in, as well as see and join existing channels. Once a channel is selected, users will be able to send and receive messages with one another in real time. 

## Goals 
Learn to use JavaScript to run code server-side.
Become more comfortable with building web user interfaces.
Gain experience with Socket.IO to communicate between clients and servers.

## Description

When you start the applicacion you will be redirected to the login page..
I will open a second tab to show the interaction between two users.
If it's the first time that the user is joinning the chat, he will need to set a display name.
After that, the user have access to the list of channels, that he's free to join to any of them, and chat with other users.
As an personal touch, I added the delete option, that each user can delete his own messages and make it invisible to the others.
If the user leave the application and reopen it, he will be redirected to the last chat that he joined.

On the backend on the static folder we can find the static folder that includes the images,stylesheets and the java script used, and on the templates folder the different html pages.
On the main JavaScript file contains the code when a DOM is loaded. Setting up channel links, buttons, etc. Sending XMLHTTP request as well as 'full-duplex communication' using Websockets and controlling of CSS animation states. 

Finally, on the application file you can find the different functions and sockets created.