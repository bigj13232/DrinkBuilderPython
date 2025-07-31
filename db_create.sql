use drinkdb;
CREATE TABLE ratings (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    drink_id INT NOT NULL,
    drink_rating DECIMAL(3, 2) NOT NULL,
    drink_user_total DECIMAL(10, 2) NOT NULL,
    drink_rating_total DECIMAL(10, 2) NOT NULL,
    drink_reviews_qty INT NOT NULL,
    FOREIGN KEY (drink_id) REFERENCES drinks(id)
);