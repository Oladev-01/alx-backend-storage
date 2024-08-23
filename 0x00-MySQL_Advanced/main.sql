DELIMITER //

CREATE TRIGGER update_item
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity in the items table based on the newly inserted order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;