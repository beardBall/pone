CREATE DATABASE knights;
use knights;

CREATE TABLE favorite_colors (
  name VARCHAR(20),
  color VARCHAR(10)
);


CREATE TABLE tasks (
  id INT AUTO_INCREMENT,
  content VARCHAR(255),
  date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);



INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
    ('Arthur', 'red'),
    ('Gawain', 'green'),
    ('Bors', 'yellow'),
    ('Bedivere', 'red'),
  ('Galahad', 'yellow');



  INSERT INTO tasks
  (content)
  VALUES
("Go to bbg"),
("Go to the gym"),
("Go to the store"),
("Go to the bar"),
("Go to the club"),
("Go to the party");