function insertStudent(name, age) {
  // Replace `studentdb` with your database object
  const studentdb = require('./path/to/database');

  const query = 'INSERT INTO STUDENTS (NAME, AGE) VALUES ($1, $2);';

  try {
    await studentdb.all();

    studentdb.run(`${query}`, [name, parseInt(age)]);
    console.log('New record added successfully!');
  } catch (error) {
    console.error('Error occurred while adding new record: ', error);
  }
}
