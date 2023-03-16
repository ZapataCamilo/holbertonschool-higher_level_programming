-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT `name`, `id`
from `cities`
where `state_id` IN(
    SELECT `id`
    FROM `states`
    WHERE `name` = `california`
);
ORDER BY `id`;
