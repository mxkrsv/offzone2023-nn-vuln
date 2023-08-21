const mysql = require('mysql');

// Configure your database connection details
const dbConfig = {
    host: 'your_db_host',
    user: 'your_db_user',
    password: 'your_db_password',
    database: 'your_db_name'
};

function addStudent(name, age, callback) {
    const connection = mysql.createConnection(dbConfig);

    connection.connect(error => {
        if (error) {
            console.error('Error connecting to the database:', error);
            callback(error);
            return;
        }

        const sql = 'INSERT INTO STUDENTS (NAME, AGE) VALUES (?, ?)';
        connection.query(sql, [name, age], (error, results) => {
            connection.end(); // Close the connection

            if (error) {
                console.error('Error inserting data:', error);
                callback(error);
                return;
            }

            console.log('Data inserted:', results);
            callback(null, results);
        });
    });
}

// Usage example
addStudent('John Doe', 25, (error, results) => {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log('Insert success:', results);
    }
});
