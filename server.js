const express = require('express');
const server = express();
const body_parser = require('body-parser')

server.listen(80, () => {
	console.log("Server is running");
});

server.use(express.static('public'))
server.use(body_parser.urlencoded({extended: true}))
server.use(body_parser.json())

server.post('/api', (req, res) => {
	console.log(req.body.ip)
});
