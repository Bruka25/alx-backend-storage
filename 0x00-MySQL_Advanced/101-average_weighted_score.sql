-- Drop the procedure if it exists already
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    -- Add temporary columns to store intermediate calculations
    ALTER TABLE users ADD total_weighted_score INT NOT NULL;
    ALTER TABLE users ADD total_weight INT NOT NULL;

    -- Calculate total weighted score for each user
    UPDATE users
        SET total_weighted_score = (
            SELECT SUM(corrections.score * projects.weight)
            FROM corrections
                INNER JOIN projects ON corrections.project_id = projects.id
            WHERE corrections.user_id = users.id
        );

    -- Calculate total weight (sum of project weights) for each user
    UPDATE users
        SET total_weight = (
            SELECT SUM(projects.weight)
            FROM corrections
                INNER JOIN projects ON corrections.project_id = projects.id
            WHERE corrections.user_id = users.id
        );

    -- Calculate and update average score for each user
    UPDATE users
        SET users.average_score = IF(users.total_weight = 0, 0, users.total_weighted_score / users.total_weight);

    -- Drop temporary columns after updating average score
    ALTER TABLE users
        DROP COLUMN total_weighted_score;
    ALTER TABLE users
        DROP COLUMN total_weight;
END $$

DELIMITER ;

