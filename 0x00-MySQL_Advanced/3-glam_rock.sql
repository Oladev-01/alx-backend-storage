-- getting the lifespan of a band
SELECT band_name, IFNULL(YEAR(split), 2022) - YEAR(formed) AS lifespan
FROM metal_bands
WHERE
    style LIKE '%Glam rock'