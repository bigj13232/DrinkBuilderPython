delete from drinks;
delete from ingredients;
vacuum;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='drinks';
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='ingredients';

