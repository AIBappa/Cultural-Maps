-- Create a script to install multiple PostgreSQL extensions

-- Enable the `uuid-ossp` extension for generating UUIDs
CREATE EXTENSION IF NOT EXISTS "address_standardizer";

-- Enable the `pgcrypto` extension for cryptographic functions
CREATE EXTENSION IF NOT EXISTS "fuzzystrmatch";

-- Enable the `hstore` extension for key-value store
CREATE EXTENSION IF NOT EXISTS "ogr_fdw";

-- Enable the `citext` extension for case-insensitive text
CREATE EXTENSION IF NOT EXISTS "pgrouting";

-- Enable the `postgis` extension for spatial and geographic objects
CREATE EXTENSION IF NOT EXISTS "postgis";

-- Enable the `btree_gin` extension for B-Tree indexes in GIN
CREATE EXTENSION IF NOT EXISTS "pointcloud";

-- Enable the `btree_gist` extension for B-Tree indexes in GiST
CREATE EXTENSION IF NOT EXISTS "pointcloud_postgis";

-- Enable the `fuzzystrmatch` extension for text similarity
CREATE EXTENSION IF NOT EXISTS "postgis_raster";

-- Enable the `tablefunc` extension for table functions
CREATE EXTENSION IF NOT EXISTS "postgis_sfcgal";

-- Enable the `intarray` extension for integer array operations
CREATE EXTENSION IF NOT EXISTS "postgis_tiger_geocoder";

-- Enable the `pg_trgm` extension for trigram similarity
CREATE EXTENSION IF NOT EXISTS "postgis_topology";

-- Enable the `unaccent` extension for removing accents
CREATE EXTENSION IF NOT EXISTS "unaccent";

-- Add more extensions as needed
-- CREATE EXTENSION IF NOT EXISTS "extension_name";

-- Notify user of completion
DO $$ BEGIN
    RAISE NOTICE 'Extensions installed successfully!';
END $$;
