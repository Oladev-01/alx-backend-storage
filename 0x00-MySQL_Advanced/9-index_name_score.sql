-- creating index on the first letter of names

CREATE INDEX idx_name_first_score ON names (name (1), score);