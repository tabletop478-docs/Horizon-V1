CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT ">>",
    AnnounceMedium integer
);

CREATE TABLE IF NOT EXISTS whitelisted (
    UserID integer PRIMARY KEY,
    Level integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS administrator (
    UserID integer PRIMARY KEY,
);

CREATE TABLE IF NOT EXISTS blacklist (
    UserID integer PRIMARY KEY,
    Level integer DEFAULT 0    
);

CREATE TABLE IF NOT EXISTS ally (
    GuildID integer PRIMARY KEY,
    Level integer DEFAULT 0    
);

CREATE TABLE IF NOT EXISTS enemy (
    GuildID integer PRIMARY KEY,
    Level integer DEFAULT 0    
);
