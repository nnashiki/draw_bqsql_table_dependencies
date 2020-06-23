CREATE TABLE
  `project.dataset.table6` AS
SELECT
  *
FROM
  `project.dataset.table2`
UNION ALL
SELECT
  *
FROM
  `project.dataset.table3`;
