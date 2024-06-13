-- Create a view to aggregate the number of fans by origin
CREATE OR REPLACE VIEW band_fans_by_origin AS
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin;

-- Query to rank the country origins of bands by number of fans
SELECT origin, total_fans
FROM band_fans_by_origin
ORDER BY total_fans DESC;
