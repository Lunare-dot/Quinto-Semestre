const express = require('express');

//modularizar as rotas
const router = express.Router;

const db = require('../db');

//criar as rotas: rota padrão: /api/users
//CRUD
//cadastrar usuários (CREATE) --> cadastrar --> /api/users/ (método: POST)
router.post('/', (req, res) => {
    const {nome, email} = req.body;

     /**
      * {
      *     "nome": "Fulano",
      *     "email": "fulano@email.com"
      * }
      */

    //executar a instrução SQL
    db.query('INSERT INTO users (nome, email) VALUES (?, ?)', [nome, email], (err, result) => {
        if(err) return res.status(500).send(err);
        res.status(201).json({id: result.insertId, nome, email})
    })
});

//exportas as rotas
module.exports = router;