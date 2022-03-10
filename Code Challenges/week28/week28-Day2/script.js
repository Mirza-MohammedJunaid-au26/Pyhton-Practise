var express = require('express');  
var app = express();  
const fs = require('fs')

var counter = 1;

app.get('/', function (req, res) {  
    res.send(`<html><body><h1>You Visited This Website : ${counter} Times </h1></body></html>`);
    fs.writeFileSync('./visited.txt',' ')
    fs.writeFileSync('./visited.txt',`You Visited This Website : ${counter} Times`)
    counter = counter + 1  

  });  

app.get('/reset',function(req,res){
    counter = 1
    res.send(`<html><body><h1>Reseted Successfully </h1></body></html>`)
    fs.writeFileSync('./visited.txt','!!! File Reseted !!!')
})

app.listen(8000);