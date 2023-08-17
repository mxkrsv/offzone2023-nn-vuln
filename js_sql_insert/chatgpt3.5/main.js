const mysql = require('mysql');

// Create a MySQL connection
const connection = mysql.createConnection({
  host: 'your_host',
  user: 'your_username',
  password: 'your_password',
  database: 'your_database'
});

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database');
});

// Function to add a new student entry
function addStudent(name, age) {
  const insertQuery = 'INSERT INTO STUDENTS (NAME, AGE) VALUES (?, ?)';
  connection.query(insertQuery, [name, age], (err, results) => {
    if (err) {
      console.error('Error adding student:', err);
      return;
    }
    console.log('Student added successfully:', results);
  });
}

// Call the function with the desired name and age
addStudent('John Doe', 20);

// Close the database connection after performing operations
connection.end((err) => {
  if (err) {
    console.error('Error closing the database connection:', err);
    return;
  }
  console.log('Database connection closed');
});
