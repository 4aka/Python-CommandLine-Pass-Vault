import os

create_entry_sql = 'INSERT INTO vault (site, date, username, password, is_favorite) VALUES (?, ?, ?, ?, ?)'
search_sql = 'SELECT password FROM vault WHERE site LIKE ?'
search_site = 'SELECT * FROM vault WHERE site = ?'
create_table_sql = 'CREATE TABLE IF NOT EXISTS vault (site TEXT, date BLOB, username BLOB, password BLOB, is_favorite BOOLEAN)'
show_favorites_sql = 'SELECT site FROM vault WHERE is_favorite = True'
select_username = 'SELECT username FROM vault WHERE site LIKE ?'
select_is_favorite = 'SELECT is_favorite FROM vault WHERE site = ?'
select_date = 'SELECT date FROM vault WHERE site = ?'
delete_row = 'DELETE FROM vault WHERE site = ?'
select_all = 'SELECT * FROM vault'
update_favorites = 'UPDATE vault SET is_favorite = TRUE WHERE site = ?'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
passowrd_file = ROOT_DIR + '\\vault.pswd'
vault_file_path = ROOT_DIR + '\\vault.db'
vault_file = 'vault.db'

hash_count = 200567
hash_count_db = 200569
date_db = 16
