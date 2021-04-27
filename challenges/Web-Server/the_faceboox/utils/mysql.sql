create database thefaceboox;
use thefaceboox;

create table messages(id serial, from_user int, to_user int, msg text);
create table students(id serial, mail text, passwd text, postfix_hash_salt text, first_name text);
create table press(id serial, user text, passwd text);

insert into students(mail, passwd, postfix_hash_salt, first_name) values('mike.spen@harvard.edu', 'a1a93242bea0cd80285ccfaf69ff96b1', '7heF@c3b00x', 'Mike');
insert into students(mail, passwd, postfix_hash_salt, first_name) values('laura00@aol.com', 'cb24a277e4b0c98e2d5eefbc17b2e658', '7heF@c3b00x', 'Laura');
insert into students(mail, passwd, postfix_hash_salt, first_name) values('kev.rgn@caramail.com', 'a066fcee06d941af7c0dfbdd05c4cda3', '7heF@c3b00x', 'Kevin');
insert into students(mail, passwd, postfix_hash_salt, first_name) values('rachel.west@fox-news.com', 'a8a2ddbeeff303b0694e480c32c8ae6c', '7heF@c3b00x', 'Rachel');

insert into press(user, passwd) values('demo','');
insert into press(user, passwd) values('cnn','');
insert into press(user, passwd) values('nyt','');
insert into press(user, passwd) values('guardian','');
insert into press(user, passwd) values('fox','');

insert into messages(from_user, to_user, msg) values(0, 0, "test message");