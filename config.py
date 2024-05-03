def read_env_file(file_path):
    env_vars = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                env_vars[key] = value
    return env_vars

env_vars = read_env_file('.env')

BOT_TOKEN = env_vars.get('BOT_TOKEN')
ADMINS_IDS = [int(id) for id in env_vars.get('ADMINS_IDS', '').split(',') if id]
DB_FILENAME = env_vars.get('DB_FILENAME', 'bot.db')