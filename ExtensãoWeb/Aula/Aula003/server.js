const express = require('express')
const app = express()
const port = 3000

//rotas -- rota padrão (/)
app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/sobre', (req, res) => {
  res.send('Página Sobre!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})