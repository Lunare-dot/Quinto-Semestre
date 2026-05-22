const express = require('express');

//modularizar as rotas
const router = express.Router();

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

//listar os usuários (READ)
router.get('/', (req, res) => {
    //executar a instrução SQL
    db.query('SELECT * FROM users', (err, results) => {
        if(err) return res.status(500).send(err);
        res.json({users: results});
    });
});

//atualizar os dados de um usuário (UPDATE): /api/users/:id
router.put('/:id', (req, res) => {
    const {nome, email} = req.body; //buscar os dados fornecidos pelo usuário
    const {id} = req.params;

    //executa a instrução SQL
    db.query('UPDATE users SET nome = ?, email = ? WHERE id = ?', [nome, email, id], (err) => {
        if(err) return res.status(500).send(err);
        res.json({id, nome, email}); //devolver a resposta ao usuário
    });
});

//excluir um usuário (DELETE): /api/users/:id
//testar: /api/users/1 (método: DELETE)
router.delete('/:id', (req, res) => {
    const {id} = req.params; //pegar o ID do usuário no front
    //executar a instrução SQL
    db.query('DELETE FROM users WHERE id = ?', [id], (err) => {
        if(err) return res.status(500).send(err);
        res.sendStatus(204);
    });
});

//exportas as rotas
module.exports = router;