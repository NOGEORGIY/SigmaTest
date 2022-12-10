const http = require("http");

const host = 'localhost';
const port = 8010;

const requestListener = function (req, res) {
    res.writeHead(200);
    res.end("3d9e8599");
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});
