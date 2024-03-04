# Streaming Live Demo by D-ID

## New Feature:
Add socket.io to send message from python client

## Initial Setup:
* (install necessary packages) open a terminal in the folder and run  - npm install
* (add your api key) edit the `api.json` inside the uncompressed folder and replace the emoji with your key

```json
{
  "key":"Add_Your_API_KEY_HERE",
  "url": "https://api.d-id.com"
}
```


## Start the demo:
* (bring up the app) in the folder (ctr left click on folder through finder) open the terminal run node app.js 
* You should see this message - server started on port localhost:4000
* (open the app) in the browser add localhost:4000
* (connect) press connect you should see the connection ready 
* (stream) run client.py to send message to the server.
