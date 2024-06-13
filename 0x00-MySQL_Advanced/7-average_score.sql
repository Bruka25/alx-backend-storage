-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Change the delimiter to $$
DELIMITER $$

-- Create the procedure
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    -- Declare variables to store total score and number of projects
    DECLARE total_score INT DEFAULT 0;
    DECLARE projects_count INT DEFAULT 0;

    -- Calculate the total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Calculate the number of projects for the user
    SELECT COUNT(*) INTO projects_count
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update the average_score for the user in the users table
    -- If projects_count is 0, set average_score to 0 to avoid division by zero
    UPDATE users
    SET users.average_score = IF(projects_count = 0, 0, total_score / projects_count)
    WHERE users.id = user_id;
END $$

-- Reset the delimiter to default
DELIMITER ;
