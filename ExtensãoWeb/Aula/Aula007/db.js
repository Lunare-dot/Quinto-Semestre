const mysql = require('mysql2');

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'admin123', //trocar para catolica
    database: 'userdb',
    port: '3306' //ou 3307
});

db.connect(err =>{
    if(err) throw err;
    console.log('conectado ao banco de dados');
});

module.exports = db;
