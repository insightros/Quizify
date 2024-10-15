from hashlib import sha256

def hash_password(password):
    """Hash the password using SHA-256."""
    return sha256(password.encode()).hexdigest()

def format_date(date):
    """Format the date in 'YYYY-MM-DD' format."""
    return date.strftime('%Y-%m-%d')
