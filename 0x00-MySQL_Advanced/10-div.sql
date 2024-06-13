-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Change the delimiter to $$
DELIMITER $$

-- Create the function
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    -- Declare and initialize result variable
    DECLARE result FLOAT DEFAULT 0;

    -- Check if b is not zero, then perform division
    IF b != 0 THEN
        SET result = a / b;
    END IF;

    -- Return the result of the division or 0 if b is 0
    RETURN result;
END $$

-- Reset the delimiter to default
DELIMITER ;
