-- Sanity checks
SELECT 1 AS health_check;
SELECT version();
SELECT current_database() AS db, current_user AS "user", inet_server_port() AS port;
