-- creating a stored procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER / /

CREATE PROCEDURE AddBonus(IN user_id INT, IN p_name VARCHAR(50), IN project_score INT)
BEGIN
    INSERT INTO projects(project_name)
    SELECT p_name
    WHERE NOT EXISTS(SELECT 1 FROM projects WHERE project_name = p_name);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, (SELECT id from projects WHERE project_name = p_name), project_score);
END //

DELIMITER ;