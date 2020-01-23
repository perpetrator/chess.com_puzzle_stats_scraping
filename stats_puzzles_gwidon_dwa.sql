CREATE TABLE `stats_puzzles_gwidon_dwa` (
  `Date` datetime DEFAULT NULL,
  `ID` bigint(20) DEFAULT NULL,
  `Rating` bigint(20) DEFAULT NULL,
  `Moves` text,
  `Target Time` text,
  `My Time` text,
  `Avg Time` text,
  `Outcome` text,
  `My Rating` bigint(20) DEFAULT NULL,
  `Number` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Number`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin2;
