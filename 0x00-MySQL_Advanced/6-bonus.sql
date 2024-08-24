-- creating a stored procedureDROP PROCEDURE IF EXISTS AddBonus;

DELIMITER / /

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Insert the project if it does not exist
    INSERT INTO projects(name)
    SELECT project_name
    WHERE NOT EXISTS(SELECT 1 FROM projects WHERE projects.name = project_name);

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE projects.name = project_name), score);
END //

DELIMITER;