const express = require('express');
const fetch = require('node-fetch');
const { Pool } = require('pg');

const app = express();
const port = process.env.PORT || 3000; // Use the desired port for your server

const dbConfig = {
  user: 'postgres',
  host: 'localhost',
  database: 'Batondb',
  password: 'Admin123',
  port: 5432 // Change to your PostgreSQL port if it's different
};

const pool = new Pool(dbConfig);

app.get('/', async (req, res) => {
  try {
    const response = await fetch('https://ipinfo.io/json');
    
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }
    
    const data = await response.json();

    const {
      ip,
      hostname,
      city,
      region,
      country,
      loc,
      org,
      postal,
      timezone,
      readme
    } = data;

    // Insert the data into the PostgreSQL database
    const query = `
      INSERT INTO visitor_data (ip_address, hostname, city, region, country, loc, org, postal, timezone, readme)
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
      RETURNING id, timestamp;
    `;

    const result = await pool.query(query, [
      ip,
      hostname,
      city,
      region,
      country,
      loc,
      org,
      postal,
      timezone,
      readme
    ]);

    console.log('Data saved to the database:', result.rows[0]);
    
    // Send a response to the client
    res.send('Data logged successfully!');
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Error logging data.');
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
