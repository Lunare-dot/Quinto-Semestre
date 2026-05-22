const express = require('express');
const app = express();
const port = 3000;

//definir o caminho
const path = require('path');
//disponibilizar os arquivos
app.use(express.static(path.join(__dirname, 'public')));

const db = require('./db');

//criar uma rota de teste
app.get('/', (req, res)=>{
    //res.send("Front funcionando - agora com o Nodemon");
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const apiRoutes = require('./routes/api') //puxar as rotas de API de usuários
app.use(express.json()); //tratar requisição JSON
app.use('/api/users', apiRoutes); //alcançar as rotas criadas no arquivo "api.js"

app.listen(port, ()=>{
    console.log("servidor funcionando");
})