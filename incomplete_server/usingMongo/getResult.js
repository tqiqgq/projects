
function getResult(searching_string) {
console.log("Start index and search")
console.log(searching_string)//!!!!!!!!!!! DELETE!!!!!!!!!!
var sleep = require('system-sleep');
  var PythonShell = require('python-shell');
  PythonShell.run('search.py', function (err,res1) {
  if (err) throw err;
  console.log(res1)
  console.log('finished');//!!!!!!!!!!! DELETE!!!!!!!!!!
});
  
  console.log("\n#############################",
              "\n# Выполняется поиск данных !",
              "\n#############################\n");
  sleep(15000);
  var MongoClient = require('mongodb').MongoClient;
  var assert = require('assert');
  var url = 'mongodb://localhost:27017/';

  var final_result = [];

  var a = new Object(); //!!!!!!!!!!! DELETE!!!!!!!!!!

  MongoClient.connect(url, function(err, db) {

    assert.equal(null, err);
    //console.log("Connected correctly to server.");
    var collection = db.collection("users");
    console.log("Загрузка данных ...");
///////////////
    //var count = collection.count({"result": searching_string});
    var cursor = collection.find({"result": searching_string});
    cursor.each(function(err, doc){
        //console.log("cursor each");
        console.log(doc);
        if (err) console.log(err);
        if (typeof(doc) =='object' && typeof(final_result) == 'object') {
          //delete doc._id;
        //delete doc.result;
        final_result.push(doc);
        console.log(typeof(final_result));
          //db.close();
        }
          else console.log("NULL"); return final_result;
          //console.log("NULL");
      });
      //console.log(doc);
      db.close();
    });
  return final_result;
    
        
     /* if (doc == null){
        console.log("doc == null")//!!!!!!!!!!! DELETE!!!!!!!!!!
          console.log(final_result)//!!!!!!!!!!! DELETE!!!!!!!!!!
          return final_result
      }*/
      
      //console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
      //console.log(doc);
      //console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
      

      //final_result.push(doc)


      //console.log(typeof(doc));
      /*Object.keys(doc).forEach(function(key1){
        console.log(typeof(key1));
        console.log(typeof(doc[key1]));
        final_result.push({key1: doc[key1]});
      });*/

      //console.log(final_result)
      //console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

      //db.close();
  //console.log(final_result)//!!!!!!!!!!! DELETE!!!!!!!!!!
  
}

module.exports = getResult;
