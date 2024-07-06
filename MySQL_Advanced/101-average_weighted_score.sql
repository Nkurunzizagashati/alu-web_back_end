-- Advanced Question
-- Show and compute average weighted score
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE avg_weighted_score FLOAT;

    DECLARE cur_users CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur_users;
    read_loop: LOOP
        FETCH cur_users INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        INTO avg_weighted_score
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        UPDATE users
        SET average_score = avg_weighted_score
        WHERE id = user_id;
    END LOOP;

    CLOSE cur_users;
END //

DELIMITER ;
