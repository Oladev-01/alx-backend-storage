-- computing average score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER / /

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE av_score DECIMAL(10, 2);
    SELECT AVG(score) INTO av_score FROM corrections WHERE
    corrections.user_id = user_id;
    UPDATE users
    SET average_score = av_score
    WHERE id = user_id;
END //

DELIMITER ;