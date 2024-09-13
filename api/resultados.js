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

router.get('/', (req, res) => {
  connection.query('SELECT * FROM resultados ORDER BY id DESC LIMIT 10', (error, results) => {
    if (error) {
      return res.status(500).json({ error: error.message });
    }
    res.json(results);
  });
});

module.exports = router;
