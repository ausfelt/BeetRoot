-- Create a table
CREATE TABLE sample_table (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);

-- Rename the table
ALTER TABLE sample_table RENAME TO renamed_table;

-- Add a new column
ALTER TABLE renamed_table ADD COLUMN occupation TEXT;

-- Insert rows into the table
INSERT INTO renamed_table (id, name, age, occupation)
VALUES (1, 'John Doe', 30, 'Engineer'),
       (2, 'Jane Smith', 25, 'Teacher');

-- Update a row
UPDATE renamed_table
SET age = 31
WHERE id = 1;

-- Delete a row
DELETE FROM renamed_table
WHERE id = 2;