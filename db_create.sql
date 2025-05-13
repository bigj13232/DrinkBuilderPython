use drinksdb;
CREATE TABLE reviews (
    review_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    drink_id INT NOT NULL,
    review_date TEXT NOT NULL,
    review TEXT NOT NULL
);
