-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked in ascending order of tv_shows.title and tv_show_genre.genre_id
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
