drop database if EXISTS awesome;
CREATE database awesome;
use awesome;

CREATE TABLE users(
  `id` varchar(50) not null,
  `email` varchar(50) not null,
  `passwd` varchar(50) not null,
  `admin` bool not null,
  `name` varchar(50) not null,
  `image` varchar(500) not null,
  `created_at` real not null,
  unique key `idx_email` (`email`),
  key `idx_created_at` (`created_at`),
  PRIMARY KEY (`id`)
) engine=innodb DEFAULT charset=utf8;

CREATE TABLE blogs(
  `id` varchar(50) not null,
  `user_id` varchar(50) not null,
  `user_name` varchar(50) not null,
  `user_image` varchar(500) not null,
  `name` varchar(50) not null,
  `summary` varchar(200) not null,
  `content` mediumtext not null,
  `created_at` real not null,
  key `idx_created_at` (`created_at`),
  PRIMARY KEY (`id`)
) engine=innodb DEFAULT charset=utf8;

CREATE TABLE comments(
  `id` varchar(50) not null,
  `blog_id` varchar(50) not null,
  `user_id` varchar(50) not null,
  `user_name` varchar(50) not null,
  `user_image` varchar(500) not null,
  `content` mediumtext not null,
  `created_at` real not null,
  key `idx_created_at` (`created_at`),
  PRIMARY KEY (`id`)
) engine=innodb DEFAULT charset=utf8;