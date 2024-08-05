-- Need to run this in destination database where data will be transferred--
-- This is applicable for copying a table from one database to another provided both are on the same server--
-- Incomplete method as columns and datatypes have to be noted --
-- However PGAdmin4 provides a much better interface, learn PAGADmin4--
CREATE EXTENSION dblink;

INSERT INTO p1backend_place
SELECT *
FROM dblink('dbname=udemyp1 user=postgres password=true3',
            'SELECT * FROM p1backend_place_v1')
AS t(column1 datatype, column2 datatype, ...);

