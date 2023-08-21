async function addStudentToDatabase(name, age) {
  const apiUrl = 'https://your-backend-api-url.com/addStudent'; // Replace with your actual API URL

  const requestBody = {
    name: name,
    age: age
  };

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    });

    if (!response.ok) {
      throw new Error('Failed to add student to database');
    }

    const responseData = await response.json();
    return responseData; // This might contain success status or newly added student details
  } catch (error) {
    console.error('Error adding student:', error);
    throw error;
  }
}

// Usage example
const studentName = 'John Doe';
const studentAge = 20;

addStudentToDatabase(studentName, studentAge)
  .then(response => {
    console.log('Student added:', response);
  })
  .catch(error => {
    console.error('Error:', error);
  });
