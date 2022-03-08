var http = require('http'); 
var randomColor = require('randomcolor'); 
const ef = require("everyday-fun");
var color = randomColor();

var server = http.createServer(function (req, res) { 
    if (req.url == '/'){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('<html><body><h3>/randomColor</h3><h3>/currentDate</h3><h3>/joke</h3><h3>/quote</h3><h3>/riddle</h3></body></html>');
        res.end();
    }
    if (req.url == '/randomColor'){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write("Random Color is : "+randomColor());
        res.end();
    }
    else if(req.url == '/currentDate'){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        d = new Date();
        res.write("Current Time is : "+d);
        res.end();
    }
    else if(req.url == '/joke'){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        jk = ef.getRandomJoke();
        res.write("Joke of the Day : "+jk.body)
        res.end();
    }
    else if(req.url == '/quote'){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        qu = ef.getRandomQuote();
        res.write("Quote : "+qu.quote)
        res.write("</br>")
        res.write("Author :"+qu.author)
        res.end();
    }
    else if(req.url == '/riddle'){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        rd = ef.getRandomRiddle();
        res.write("Question : "+rd.riddle)
        res.write("</br>")
        res.write("Answer :"+rd.answer)
        res.end();
    }
});

server.listen(8000); 

console.log('Node.js web server at port 8000 is running..')