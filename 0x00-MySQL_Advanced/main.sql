DELIMITER //

CREATE TRIGGER update_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Update the quantity in the items table based on the newly inserted order
    IF OLD.email <> NEW.email THEN
        IF OLD.valid_email = 0 THEN
            SET NEW.valid_email = 1;
        ELSE
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END //

DELIMITER ;