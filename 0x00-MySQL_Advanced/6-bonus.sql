-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS AddBonus;

-- Change the delimiter to $$
DELIMITER $$

-- Create the procedure
CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project already exists
    SELECT id INTO project_id
    FROM projects
    WHERE name = p_project_name
    LIMIT 1;

    -- If the project does not exist, create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (p_project_name);
        
        -- Get the new project's id
        SELECT LAST_INSERT_ID() INTO project_id;
    END IF;

    -- Insert the new correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (p_user_id, project_id, p_score);
END $$

-- Reset the delimiter to default
DELIMITER ;
