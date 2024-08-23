-- making an update based on some condition

DELIMITER / /

CREATE TRIGGER
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        IF NEW.valid_email = 0 THEN
            SET NEW.valid_email = 1;
        ELSE
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END //

DELIMITER;
