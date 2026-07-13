const express=require('express');
const { Pool}=require('pg');
const cors = require('cors');

const app = express();
const PORT = 8000;

app.use(cors());
app.use(express.json());

const pool=new Pool({
	user:'app_user',
	host:'127.0.0.1',
	database:'app_db',
	password:'ehf,jhjc',
	port:5432,
});

app.get('/tasks',async (req,res)=>{
	try{
		const result=await pool.query('SELECT title FROM tasks;');
		const tasks = result.rows.map(row => row.title);
	        res.json(tasks);
} catch (err) {
        res.status(500).json({ error: err.message });
    }
});
// POST-запрос: записываем новую задачу в базу данных
app.post('/tasks', async (req, res) => {
    const { title } = req.body;
    try {
        await pool.query('INSERT INTO tasks (title) VALUES ($1);', [title]);
        res.json({ status: 'success' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(PORT, () => {
    console.log(`Бэкенд на JavaScript запущен на http://127.0.0.1:${PORT}`);
});
