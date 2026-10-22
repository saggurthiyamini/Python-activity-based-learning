# Case Study 29: Password Policy Validation Engine

password = input("Enter a sample password: ")
prohibited = ["password", "123456", "admin"]
errors = []

if len(password) < 8:
    errors.append("Must contain at least 8 characters.")
if not any(ch.islower() for ch in password):
    errors.append("Must contain a lowercase letter.")
if not any(ch.isupper() for ch in password):
    errors.append("Must contain an uppercase letter.")
if not any(ch.isdigit() for ch in password):
    errors.append("Must contain a digit.")
if not any(not ch.isalnum() for ch in password):
    errors.append("Must contain a special character.")
if any(password[i] == password[i + 1] == password[i + 2] for i in range(len(password) - 2)):
    errors.append("Must not contain the same character three times consecutively.")
if any(word in password.lower() for word in prohibited):
    errors.append("Contains a prohibited substring.")

if errors:
    print("\nPassword is INVALID:")
    for error in errors:
        print("-", error)
else:
    print("\nPassword satisfies all sample policy rules.")
