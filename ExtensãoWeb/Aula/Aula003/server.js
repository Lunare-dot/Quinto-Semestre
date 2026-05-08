const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded({extended: true}));

//trabalhar com arquivos estáticos
app.use(express.static('public'));

//rotas -- rota padrão (/)
app.get('/', (req, res) => {
  //res.send('Hello World!')
  res.sendFile(__dirname + '/public/Html/index.html');
})

app.get('/sobre', (req, res) => {
  //res.send('Página Sobre!')
  res.sendFile(__dirname + '/public/Html/sobre.html');
})

app.post('/contato', (req, res) => {
  const{nome, email} = req.body;
  res.send(`Dados cadastrados!
    <br>Nome: ${nome}
    <br>Email: ${email}`);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})