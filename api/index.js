const express = require('express');
const resultadosRouter = require('./resultados');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use('/resultados', resultadosRouter);

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
