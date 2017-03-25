-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Create Database

create database tournament ;

--Connect to new database
\c tournament ;

--Create table to store Participants 
create table players (
id serial primary key,
name varchar(50) not null) ;

--Create table to store the matches.
create table matches (
id serial primary key,
winner smallint references players(id),
loser smallint references players(id)) ;