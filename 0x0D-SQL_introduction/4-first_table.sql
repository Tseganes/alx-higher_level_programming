-- creates a tabel first_table in current db in ur MYSQL server
-- does not fail if table exists
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
