create table clan (
  clan_id        varchar(15) not null,
  clan_name      varchar(40) not null,
  primary key (clan_id)
);

create table clan_player (
  clan_id        varchar(15) not null,
  player_id      varchar(15) not null,
  as_of_datetime timestamp not null,
  primary key (clan_id, player_id)
);

create table player (
  player_id               varchar(15) not null,
  first_known_player_name varchar(40) not null,
  player_welcome          tinyint     not null,
  primary key (player_id)
);

create table player_progress (
  player_id           varchar(15) not null,
  as_of_datetime      timestamp not null,
  current_player_name varchar(40) not null,
  troops_donated      integer not null,
  troops_received     integer not null,
  friend_in_need      integer not null,
  war_hero            integer not null,
  sharing_is_caring   integer not null,
  games_champion      integer not null,
  primary key (player_id, as_of_datetime)
);
