-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Change the delimiter to $$
DELIMITER $$

-- Create the function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE result DECIMAL(10,2);
    
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    
    RETURN result;
END $$

-- Reset the delimiter to default
DELIMITER ;
