CREATE TABLE IF NOT EXISTS sandbox.regions (
region TEXT PRIMARY KEY,
manager TEXT
);

INSERT INTO sandbox.regions (region, manager) VALUES
('West','Alex'),('East','Sam');
