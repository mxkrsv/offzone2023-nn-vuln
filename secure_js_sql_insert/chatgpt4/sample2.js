async function addStudent(name, age) {
    try {
        const response = await fetch('http://your_server_url:3000/addStudent', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, age })
        });

        if (response.status !== 200) {
            const errorMessage = await response.text();
            throw new Error(errorMessage);
        }
        
        console.log('Student added successfully.');
    } catch (error) {
        console.error('Error adding student:', error.message);
    }
}

// Usage
addStudent('John Doe', 25);
