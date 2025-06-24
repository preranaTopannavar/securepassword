import hashlib
import requests
import re

def check_strength(password):
    if len(password) < 8:
        return "Weak password: must be at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return "Weak password: include an uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Weak password: include a lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Weak password: include a number."
    if not re.search(r"[!@#$%^&*()_+=\-]", password):
        return "Weak password: include a special character."
    return "Strong password."

def check_breach(password):
    sha1_pw = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1_pw[:5], sha1_pw[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5}"
    res = requests.get(url)
    if res.status_code != 200:
        return "Could not check breach status."
    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return f"⚠️ This password has appeared in {count} breaches!"
    return "✅ This password has not been found in known breaches."
