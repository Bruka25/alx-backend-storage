-- Change the delimiter to $$
DELIMITER $$

-- Create the procedure
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    -- Declare variables to store total weighted score and total weight
    DECLARE total_weighted_score INT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    -- Calculate the total weighted score for the user
    SELECT SUM(corrections.score * projects.weight)
        INTO total_weighted_score
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    -- Calculate the total weight of projects for the user
    SELECT SUM(projects.weight)
        INTO total_weight
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    -- Update the average_score for the user in the users table
    IF total_weight = 0 THEN
        -- If total_weight is 0, set average_score to 0 to avoid division by zero
        UPDATE users
            SET average_score = 0
            WHERE id = user_id;
    ELSE
        -- Calculate and update average_score with total weighted score divided by total weight
        UPDATE users
            SET average_score = total_weighted_score / total_weight
            WHERE id = user_id;
    END IF;
END $$

-- Reset the delimiter to default
DELIMITER ;
