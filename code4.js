const mysql = require('mysql2')
const pool = mysql.createPool({
    host:'localhost',
    user:'root',
    database:'mydb',
    password:'root'
})

// module.exports = pool.promise()
const db = pool.promise()
const query = `insert into student values("ultron",20)`
// db.execute('select * from student')
db.execute(query)
.then((res)=>{
    console.log(res);
    db.end()
})
.catch(()=>{
    console.log("problem is there");
    db.end()
})
// npm install mysql2 --save