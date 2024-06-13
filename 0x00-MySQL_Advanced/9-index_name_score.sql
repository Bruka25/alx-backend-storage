-- Create the index if it does not exist
CREATE INDEX idx_name_first_score 
ON names (LEFT(name, 1), score);
