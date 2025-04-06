const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// ✅ MySQL DB Connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'mayusona', // your MySQL password if any
  database: 'telemedicine'
});

db.connect(err => {
  if (err) {
    console.error('DB connection failed:', err);
  } else {
    console.log('✅ Connected to MySQL');
  }
});

// 🚀 Register API
app.post('/register', (req, res) => {
  const { email, password } = req.body;

  const checkUser = 'SELECT * FROM users WHERE email = ?';
  db.query(checkUser, [email], (err, results) => {
    if (results.length > 0) {
      return res.json({ message: 'User already exists. Please login.' });
    }

    const sql = 'INSERT INTO users (email, password) VALUES (?, ?)';
    db.query(sql, [email, password], (err) => {
      if (err) {
        return res.json({ message: 'Registration failed.' });
      }
      res.json({ message: 'User registered successfully.' });
    });
  });
});

// 🔐 Login API
app.post('/login', (req, res) => {
  const { email, password } = req.body;

  const sql = 'SELECT * FROM users WHERE email = ? AND password = ?';
  db.query(sql, [email, password], (err, results) => {
    if (err) return res.json({ message: 'Error during login.' });

    if (results.length > 0) {
      res.json({ message: 'Login successful!' });
    } else {
      res.json({ message: 'User not registered. Please sign up.' });
    }
  });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});
