-- creating a stored procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER / /

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    INSERT INTO projects(project_name)
    SELECT project_name
    WHERE NOT EXISTS(SELECT 1 FROM projects WHERE project_name = project_name);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, (SELECT id from projects WHERE project_name = project_name), score);
END //

DELIMITER ;