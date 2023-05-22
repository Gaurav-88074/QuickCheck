// const options = {
//     method: 'POST',
//     headers: {'Content-Type': 'application/json'},
//     body: '{"quantity":"3"}'
//   };

//   fetch('http://127.0.0.1:8000/getvocabquestion', options)
//     .then(response => response.json())
//     .then(response => console.log(response))
//     .catch(err => console.error(err));
const fetch = require("node-fetch");
const options = {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
  // body: JSON.stringify({
  //   username : "Vision",
  //   age : 20
  // })
};

fetch("https://rough-4567a-default-rtdb.firebaseio.com/users.json",options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));