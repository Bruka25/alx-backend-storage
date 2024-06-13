-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Change the delimiter to $$
DELIMITER $$

-- Create the procedure
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Compute the average score
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update or insert into the average_scores table
    -- Assuming average_scores table exists with columns (user_id, average_score)
    -- Replace with your actual table name and column names if different
    INSERT INTO average_scores (user_id, average_score)
    VALUES (p_user_id, avg_score)
    ON DUPLICATE KEY UPDATE average_score = avg_score;

END $$

-- Reset the delimiter to default
DELIMITER ;
