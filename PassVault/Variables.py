import os

create_entry_sql = "INSERT INTO vault (site, username, password, is_faforite) VALUES (?, ?, ?, ?)"
search_sql = "SELECT password FROM vault WHERE site LIKE '%?%'"
create_table_sql = "CREATE TABLE IF NOT EXISTS vault (site TEXT, username TEXT, password BLOB, is_faforite Boolean)"
show_favorites_sql = "SELECT is_favorite FROM vault WHERE is_favorite = True"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
passowrd_file = ROOT_DIR + '\\vault.pswd'
passowrd_db_file = ROOT_DIR + '\\vault_db.pswd'
vault_file_path = ROOT_DIR + '\\vault.db'
vault_file = 'vault.db'
