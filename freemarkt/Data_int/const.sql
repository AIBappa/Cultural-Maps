SELECT conname
FROM pg_constraint
WHERE conrelid = 'p1backend_place_categories'::regclass;
