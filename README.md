multify
=======

A Open-source stereo which uses facial recognition to recognize friends faces from Facebook and then play their mutual taste of music. 


Install
=======

It's a bit tricky to install this but I'll leave some useful links on how to setup.

You'll need :

 * Python 2.7+ (Python 3+ isn't supported)
 * OpenCV with Python bindings working
 * git @ Hexxeh/spotify-websocket-api
 * git @ jackbillstrom/multify
 * Last.FM API-Key
 * Rekognition V2 API-tokens
 * Facebook Open-graph token
 * Spotify Premium with a device password
 * Webcam


1. First of all, you should install python if you don't have it installed already. 
2. Now install OpenCV, I reccomend this guide: http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html#linux-installation
3. Clone git @ Hexxeh/spotify-websocket-api 
4. Clone git @ jackbillstrom/multify
5. Get your API-tokens for all services required and replace them in the source-code
6. Put some of your friends facebook profile photos inside the Rekognition API and name them to their Facebook ID/Facebook Username
6. Put the jackbillstrom/multify files inside the Hexxeh/spotify-websocket-api/clients/respotify
7. CD into Hexxeh/spotify-websocket-api/clients/respotify
8. Start the python script 'facedetect.py --cascade-face=face.xml 0'
9. Now display a users face which is inside the Rekognition API
