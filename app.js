const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const port = 4000;

const app = express();

app.use(express.json())

app.use('/', express.static(__dirname));


const server = http.createServer(app);
const io = new Server(server);
// server-side
io.on("connection", (socket) => {
  app.post('/api', function (req, res) {
    console.log(req.body.text);
    io.emit("hello", req.body.text);
    res.send('POST request succeed');
  });
});

server.listen(port, '0.0.0.0', () => {
  console.log(`server running at http://yourcomputerip:${port}`);
});
