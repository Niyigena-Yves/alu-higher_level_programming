-- Retrieves all shows from hbtn_0d_tvshows that do not have a linked genre
-- Selects all rows from the database where there is no corresponding genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
