-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS reset_valid_email;

-- Change the delimiter to $$
DELIMITER $$

-- Create the trigger
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$

-- Reset the delimiter to default
DELIMITER ;
