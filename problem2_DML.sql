USE library_db;

INSERT INTO AUTHOR (author_id, name, country) VALUES (1, 'Naglaa Mahfouz', 'Egypt');
INSERT INTO AUTHOR (author_id, name, country) VALUES (2, 'Agatha Christie', 'UK');
INSERT INTO AUTHOR (author_id, name, country) VALUES (3, 'Dan Brown', 'USA');

INSERT INTO BOOK (book_id, title, price, author_id) VALUES (1, 'Database Systems', 150.00, 1);
INSERT INTO BOOK (book_id, title, price, author_id) VALUES (2, 'Advanced SQL', 200.50, 1);
INSERT INTO BOOK (book_id, title, price, author_id) VALUES (3, 'Murder on the Orient Express', 120.00, 2);
INSERT INTO BOOK (book_id, title, price, author_id) VALUES (4, 'The ABC Murders', 95.00, 2);
INSERT INTO BOOK (book_id, title, price, author_id) VALUES (5, 'The Da Vinci Code', 180.00, 3);
INSERT INTO BOOK (book_id, title, price, author_id) VALUES (6, 'Angels & Demons', 160.00, 3);