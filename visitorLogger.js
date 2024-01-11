import('node-fetch')
  .then(async (nodeFetch) => {
    const fetch = nodeFetch.default;
    
    // Import the 'pg' library using require
    const { Pool } = require('pg');
    
    const dbConfig = {
      user: 'postgres',
      host: 'localhost',
      database: 'Batondb',
      password: 'Admin123',
      port: 5432 // Change to your PostgreSQL port if it's different
    };
    
    const pool = new Pool(dbConfig);
    
    // Function to fetch data from https://ipinfo.io/json and save it to the database
    async function getAndSaveIPInfo() {
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
      } catch (error) {
        console.error('Error:', error);
      } finally {
        await pool.end(); // Close the database connection
      }
    }
    
    // Call the function to fetch IP info and save it to the database
    getAndSaveIPInfo();
    
  })
  .catch((error) => {
    console.error('Error importing modules:', error);
  });
