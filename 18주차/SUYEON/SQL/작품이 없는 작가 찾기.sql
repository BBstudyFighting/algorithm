SELECT o1.artist_id, o1.name
FROM artists AS o1
LEFT JOIN artworks_artists AS o2 ON o2.artist_id = o1.artist_id
WHERE death_year is not null AND artwork_id is null