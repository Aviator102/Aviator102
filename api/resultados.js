const express = require('express');
const mysql = require('mysql2');

const router = express.Router();

const connection = mysql.createConnection({
  host: 'db4free.net',
  user: 'ssonhador',
  password: 'ssonhador',
  database: 'ssonhador',
  charset: 'utf8mb4'
});

// Rota para pegar todos os registros
router.get('/', (req, res) => {
  connection.query('SELECT * FROM resultados ORDER BY id DESC LIMIT 10', (error, results) => {
    if (error) {
      return res.status(500).json({ error: error.message });
    }
    res.json(results);
  });
});

// Rota para pegar um registro específico pelo ID
router.get('/:id', (req, res) => {
  const { id } = req.params;
  
  connection.query('SELECT * FROM resultados WHERE id = ?', [id], (error, results) => {
    if (error) {
      return res.status(500).json({ error: error.message });
    }
    if (results.length === 0) {
      return res.status(404).json({ error: 'Registro não encontrado' });
    }
    res.json(results[0]);
  });
});

module.exports = router;
