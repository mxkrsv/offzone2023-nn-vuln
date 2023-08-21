async function addStudent(name, age) {
    const apiUrl = 'https://your-backend-url.com/api/students';

    // The data we are going to send in our request
    let data = {
	'NAME': name,
	'AGE': age
    };

    try {
	// Create a new student entry by sending a POST request
	const response = await fetch(apiUrl, {
	    method: 'POST',
	    headers: {
		'Content-Type': 'application/json'
	    },
	    body: JSON.stringify(data)
	});

	// Check if the request was successful
	if (response.ok) {
	    const result = await response.json();
	    console.log(result);
	} else {
	    console.error('Error adding student:', response.statusText);
	}
    } catch (error) {
	console.error('There was an error adding the student:', error);
    }
}
