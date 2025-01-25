def login(username, password):
    # Input validation
    if not username or not password:
        raise ValueError("Username and password are required.")

    # ... (Authentication logic)

    return True  # Successful login