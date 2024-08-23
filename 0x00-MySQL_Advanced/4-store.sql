-- automating the database
DELIMITER / /

CREATE TRIGGER update_item
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER;