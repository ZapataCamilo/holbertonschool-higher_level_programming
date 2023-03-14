-- creates a table second_table in the database
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    `name`  VARCHAR(256),
    score INT);

INSERT INTO second_table
VALUES
    (id=1, "John", 10),
    (id=2, "Alex", 3),
    (id=3, "Bob", 14),
    (id=4, "George", 8);
