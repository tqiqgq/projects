var
  express = require( 'express' ),
  bodyParser = require( 'body-parser' ),
  app = express();
var documents;
var appendString = require('./usingMongo/appendString');
var getResult = require('./usingMongo/getResult');

app.use( bodyParser.urlencoded( { extended: true } ) );
app.use( bodyParser.json() );
app.use(express.static(__dirname + '/public'));

/////////////////////////////////////////////////////////////////

app.get( '/', function(request, response) {
  response.render(
    'index.ejs'
  );
});

app.get( '/document/:id', function(request, response) {
  var key = request.params.id;
  response.render(
    'document.ejs', { document: documents[key-1] }
  );
});

/////////////////////////////////////////////////////////////////

var documents;
var userText;

app.get( '/search', function(request, response) {

  //documents = getResult(userText);
  //console.log("search.py GETResult")
  //console.log(typeof(documents))
  //console.log(documents)
  /*
    {
      "id": "1",
      "name": "document_#1",
      "entries": [ "entry_$1", "entry_$2", "entry_$3" ]
    },
    {
      "id": "2",
      "name": "document_#2",
      "entries": [ "entry_$4", "entry_$5", "entry_$6" ]
    },
    {
      "id": "3",
      "name": "document_#3",
      "entries": [ "entry_$7", "entry_$8", "entry_$8" ]
    }
  ];*/

  response.render(
    'search.ejs', { documents: documents }
  );
});

app.post( '/search', function(request, response) {
  userText = request.body.request;
  documents = appendString(userText);
  
  console.log(documents)
  response.redirect('/search');

} );

/////////////////////////////////////////////////////////////////

app.listen( 3000, function() {
  console.log( "server.js Listening on 3000..." );
});
