def check_password_strength(password):
    strength = 0
    remarks = ""
    
    if len(password) >= 8:
        strength += 1
    
    if any(char.islower() for char in password):
        strength += 1
        
    if any(char.isupper() for char in password):
        
    if any(char.isdigit() for char in password):
        strength += 1

    if strength == 4:
        remarks = "Very Strong"
    elif strength == 3:
        remarks = "Strong"
    elif strength == 2:
        remarks = "Moderate"
    else:
        remarks = "Weak"
        
    print(f"Strength: {remarks} ({strength}/4)")

# Test it out
check_password_strength("bqeou12A")