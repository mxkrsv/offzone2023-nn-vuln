const { Client } = require('pg'); // import the PG module

async function createStudent(name, age) {
  const client = new Client({
    connectionString: 'YOUR_CONNECTION_STRING',
  });

  await client.connect();

  async function upsertStudents() {
    const transaction = await client.transaction();

    try {
      // Start a transaction
      await transaction.doTransaction(async (transaction) => {
        // Run SQL statements inside a transaction
        await transaction.sql(`INSERT INTO students (${name}, ${age}) VALUES ('${name}', ${age});`);
      });
    } catch (error) {
      console.log("Error occurred during transaction", error);
    } finally {
      // Always commit or rollback the transaction
      await transaction.end();
    }
  }

  return upsertStudents();
}

createStudent('John Doe', 20).then((result) => {
  console.log(result);
}).catch(err => {
  console.error(err);
});

// Call close when done to release resources
client.close();
console.info("Done!");
