function appendString(userText) {
  var result  = [];

  var MongoClient = require('mongodb').MongoClient;
  
  var assert = require('assert');
  var url = 'mongodb://localhost:27017/';
  MongoClient.connect(url, function(err, db) {

    assert.equal(null, err);
    // console.log("Connected correctly to server.");
    var collection = db.collection("users");
    var SearchingString = {"Searchstring": userText};
    collection.insertOne(SearchingString, function(err, result){
      if(err){
        return console.log(err);
      }
      db.close();});

  });





//var execSync = require('exec-sync');

//var user = execSync('python search.py');

/*function python_search(){


var PythonShell = require('python-shell'); // 
console.log("start python")
  PythonShell.run('search.py', function (err,res1) {

  if (err) throw err;
  console.log(res1)
  console.log('finished');//!!!!!!!!! DELETE!!!!!!!!!!
});

console.log("end python")


}

 python_search()// к сожалению не смог решить, как сделать выполнение друг за другом
// Асинхронность одним словом
 setTimeout('n=1', 10000);*/
/*
var PythonShell = require('python-shell');
var pyshell = new PythonShell('search.py');

//PythonShell.run('search.py', function (err) {
    //if (err) throw err;
    //console.log('finished_run');
//});
pyshell.on('data', function (err) {
    if (err) throw err;
    console.log('finished_on');
});

pyshell.end(function (err) {
    if (err) throw err;
    console.log('finished_end');
});
*/
// SOCKET SERVER
console.log("appendString.js socket server")
var net = require('net');

var HOST = 'localhost';
var PORT = 4080;

// Create a server instance, and chain the listen function to it
// The function passed to net.createServer() becomes the event handler for the 'connection' event
// The sock object the callback function receives UNIQUE for each connection
var server = net.createServer(function(sock) {
    
    // We have a connection - a socket object is assigned to the connection automatically
    console.log('CONNECTED: ' + sock.remoteAddress +':'+ sock.remotePort);
    
    // Add a 'data' event handler to this instance of socket
    sock.on('data', function(data) {
        console.log("appendString.js sock data")
        server.unref()
        if (data == 'close') {
          console.log("appendString.js close server-socket")
          server.close()
        };
        result.push(data);

        // console.log('DATA ' + sock.remoteAddress + ': ' + data);
        // Write the data back to the socket, the client will receive it as data from the server
        // sock.write('You said "' + data + '"');
        
    });
    
    // Add a 'close' event handler to this instance of socket
    sock.on('close', function(data) {
        console.log('CLOSED: ' + sock.remoteAddress +' '+ sock.remotePort);
    });
    
}).listen(PORT, HOST);

//console.log('Server listening on ' + HOST +':'+ PORT);
//console.log(result);
return result;

}

module.exports = appendString;

