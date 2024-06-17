SELECT avg(energy) FROM songs where artist_id =
    (SELECT id FROM artists WHERE name = 'Drake');
