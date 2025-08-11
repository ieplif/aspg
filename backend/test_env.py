import os

# Testando o caminho do arquivo .env
config_file = r"C:\Users\filipe.ribeiro\Desktop\aspg\aspg\backend\app\core\config.py"
env_file_path = os.path.join(os.path.dirname(config_file), "../../../../.env")
env_file_path_resolved = os.path.abspath(env_file_path)

print(f"Config file: {config_file}")
print(f"Env file path relative: {env_file_path}")
print(f"Env file path resolved: {env_file_path_resolved}")
print(f"Env file exists: {os.path.exists(env_file_path_resolved)}")

if os.path.exists(env_file_path_resolved):
    print("Conteúdo do arquivo .env:")
    with open(env_file_path_resolved, 'r') as f:
        print(f.read())
