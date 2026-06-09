-- row count
SELECT COUNT(*) AS total_rows
FROM smhi_air_temperature_latest_hour;

-- observation time range
SELECT
    MIN(observation_time) AS earliest,
    MAX(observation_time) AS latest
FROM smhi_air_temperature_latest_hour;

-- number of unique stations
SELECT COUNT(DISTINCT station_id) AS station_count
FROM smhi_air_temperature_latest_hour;

-- null check on key fields
SELECT
    COUNT(*) FILTER (WHERE station_id IS NULL)    AS null_station_id,
    COUNT(*) FILTER (WHERE station_name IS NULL)  AS null_station_name,
    COUNT(*) FILTER (WHERE temperature_c IS NULL) AS null_temperature,
    COUNT(*) FILTER (WHERE latitude IS NULL)      AS null_latitude,
    COUNT(*) FILTER (WHERE longitude IS NULL)     AS null_longitude
FROM smhi_air_temperature_latest_hour;

-- quality code breakdown
SELECT quality_code, COUNT(*) AS count
FROM smhi_air_temperature_latest_hour
GROUP BY quality_code
ORDER BY count DESC;

-- temperature range
SELECT
    MIN(temperature_c) AS min_temp,
    MAX(temperature_c) AS max_temp,
    ROUND(AVG(temperature_c)::numeric, 2) AS avg_temp
FROM smhi_air_temperature_latest_hour;

-- coldest and warmest stations
SELECT station_name, temperature_c, latitude, longitude
FROM smhi_air_temperature_latest_hour
ORDER BY temperature_c ASC
LIMIT 5;

SELECT station_name, temperature_c, latitude, longitude
FROM smhi_air_temperature_latest_hour
ORDER BY temperature_c DESC
LIMIT 5;

-- sample rows
SELECT station_id, station_name, temperature_c, quality_code, observation_time
FROM smhi_air_temperature_latest_hour
LIMIT 10;
