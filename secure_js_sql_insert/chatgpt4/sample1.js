const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Connect to MySQL
const connection = mysql.createConnection({
    host: 'your_host',
    user: 'your_user',
    password: 'your_password',
    database: 'your_database'
});

connection.connect();

// Middleware
app.use(bodyParser.json());

app.post('/addStudent', (req, res) => {
    const { name, age } = req.body;
    
    if(!name || !age) {
        return res.status(400).send('Name and age are required.');
    }

    const query = 'INSERT INTO STUDENTS (NAME, AGE) VALUES (?, ?)';
    connection.query(query, [name, age], (error, results) => {
        if (error) {
            console.error(error);
            return res.status(500).send('Server Error.');
        }
        res.status(200).send('Student added successfully.');
    });
});

app.listen(port, () => {
    console.log(Server running on port ${port});
});
