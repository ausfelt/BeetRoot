-- Create a table named 'customers'
CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);

-- Rename the table 'customers' to 'clients'
ALTER TABLE customers RENAME TO clients;

-- Add a new column 'address' to the 'clients' table
ALTER TABLE clients ADD COLUMN address TEXT;

-- Insert a couple rows inside the 'clients' table
INSERT INTO clients (name, email, address) VALUES ('John Doe', 'johndoe@example.com', '123 Main St');
INSERT INTO clients (name, email, address) VALUES ('Jane Smith', 'janesmith@example.com', '456 Elm St');

-- Perform an UPDATE statement on inserted rows
UPDATE clients SET address = '789 Oak St' WHERE name = 'John Doe';

-- Perform a DELETE statement on inserted rows
DELETE FROM clients WHERE name = 'Jane Smith';