const express = require('express');
const mysql = require('mysql2/promise'); // Use 'mysql2/promise' for Promise-based API

const app = express();
const port = 3000;

// Replace with your MySQL database configuration
const dbConfig = {
  host: 'your_database_host',
  user: 'your_database_user',
  password: 'your_database_password',
  database: 'your_database_name'
};

// Create a connection pool
const pool = mysql.createPool(dbConfig);

// Middleware to parse JSON in request body
app.use(express.json());

// Route to add a new student
app.post('/add-student', async (req, res) => {
  const { name, age } = req.body;

  try {
    const connection = await pool.getConnection();
    const query = 'INSERT INTO STUDENTS (NAME, AGE) VALUES (?, ?)';
    await connection.query(query, [name, age]);
    connection.release();

    res.status(200).json({ message: 'Student added successfully' });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'An error occurred while adding the student' });
  }
});

app.listen(port, () => {
  console.log(Server is running on port ${port});
});
