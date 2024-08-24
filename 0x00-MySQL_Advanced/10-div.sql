-- Creating function
DELIMITER / /

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 6)
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;
