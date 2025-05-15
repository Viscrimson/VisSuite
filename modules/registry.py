import winreg, json

def read_keys(): ...
def write_keys(d): ...
def save_tokens(account):
    keys = read_keys()
    with open(f'tokens/{account}.json', 'w') as f:
        json.dump(keys, f)

def load_tokens(account):
    with open(f'tokens/{account}.json') as f:
        data = json.load(f)
    write_keys(data)