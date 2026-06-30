import secrets
import string
import argparse


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"

    if length < 4:
        raise ValueError("Length must be at least 4")

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password


def password_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+" for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    levels = {0: "Very Weak", 1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong", 5: "Excellent"}
    return levels[score]


def main():
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords to generate")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    args = parser.parse_args()

    for _ in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
        print(f"{pwd}  [{password_strength(pwd)}]")


if __name__ == "__main__":
    main()
