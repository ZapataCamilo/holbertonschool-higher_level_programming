-- script that lists all databases
SELECT schema_name
FROM information_schema.schemata
WHERE schema_name LIKE '%schema' OR 
      schema_name LIKE '%s';
