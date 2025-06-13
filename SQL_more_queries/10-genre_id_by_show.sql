-- Retrieves all shows from hbtn_0d_tvshows that are linked to at least one genre
-- Selects all rows from the database where there is a common column
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
