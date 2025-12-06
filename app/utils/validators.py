def require_keys(data, keys):
    missing = [k for k in keys if k not in data]
    if missing:
        raise ValueError('Missing keys: ' + ','.join(missing))
def require_keys(data, keys):
    missing = [k for k in keys if k not in data]
    if missing:
        raise ValueError('Missing keys: ' + ','.join(missing))
