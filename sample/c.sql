CREATE TABLE
  `project.dataset.table7` AS
SELECT
  *
FROM
  `project.dataset.table3`
INNER JOIN
  `project.dataset.table4`
USING
  (user_id);
