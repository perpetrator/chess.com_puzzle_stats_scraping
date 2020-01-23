# chess.com_puzzle_stats_scraping
Small script to scrap stats of your solved puzzles from chess.com

Since chess.com API does't support puzzle stats, I decided to scrap it.

How to:

1. Create database, run stats_puzzles_gwidon_dwa.sql to create table,
2. Edit config.dummy & rename to config.json,
3. Edit config.json path in chess_scraping.py (if you want to run it by cron),
4. Add it to crontab (crontab -e), for example (every 2 hours):
0 */2 * * * python ~/chess_scraping.py >> ~/chess_scraping.log

