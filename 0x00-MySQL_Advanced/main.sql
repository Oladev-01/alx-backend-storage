DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;
CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    average_score FLOAT DEFAULT 0,
    PRIMARY KEY(id)
);

CREATE TABLE projects(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE corrections(
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    score INT DEFAULT 0,
    KEY `user_id` (`user_id`),
    KEY `project_id`(`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users(name) values ("Bob");
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users(name) VALUES ("Jeanne");
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects(name) values ("C is fun");
SET @fp_id = LAST_INSERT_ID();

INSERT INTO projects(name) VALUES ("Python is cool");
SET @sp_id = LAST_INSERT_ID();

INSERT INTO corrections(user_id, project_id, score) VALUES
    (@user_bob, @fp_id, 80),
    (@user_bob, @sp_id, 96),
    (@user_jeanne, @fp_id, 91),
    (@user_jeanne, @sp_id, 73);
