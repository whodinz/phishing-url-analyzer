# Phishing URL Analyzer
# Author: Dinidu Pieris
# Version: 1.0

print("=" * 50)
print("        🔎 PHISHING URL ANALYZER")
print("=" * 50)

url = input("\nEnter a URL to analyze: ")

print("\n" + "-" * 50)
print(f"Analyzing: {url}")
print("-" * 50)

# HTTPS Check
if url.startswith("https://"):
    print("HTTPS:               ✅ Secure connection")
else:
    print("HTTPS:               ⚠️ No HTTPS detected")

# IP Address Check
parts = url.split("/")

if len(parts) > 2 and all(part.isdigit() for part in parts[2].split(".")):
    print("IP Address:          ⚠️ URL uses an IP address")
else:
    print("IP Address:          ✅ Normal domain detected")

# Suspicious Keywords Check
suspicious_words = [
    "login",
    "verify",
    "account",
    "password",
    "update",
    "secure"
]

found_words = []

for word in suspicious_words:
    if word in url.lower():
        found_words.append(word)

if found_words:
    print(f"Suspicious Keywords:  ⚠️ Found {', '.join(found_words)}")
else:
    print("Suspicious Keywords:  ✅ None detected")

# URL Length Check
if len(url) > 75:
    print("URL Length:           ⚠️ Unusually long URL")
else:
    print("URL Length:           ✅ Normal length")

# Domain Length Check
domain = parts[2] if len(parts) > 2 else ""

if len(domain) > 30:
    print("Domain Length:        ⚠️ Unusually long domain")
else:
    print("Domain Length:        ✅ Normal domain length")

# Suspicious Characters Check
suspicious_chars = ["@", "%", "\\"]

found_chars = []

for char in suspicious_chars:
    if char in url:
        found_chars.append(char)

if found_chars:
    print(f"Suspicious Characters: ⚠️ Found {', '.join(found_chars)}")
else:
    print("Suspicious Characters: ✅ None detected")

# Risk Score
risk_score = 0

if not url.startswith("https://"):
    risk_score += 2

if len(parts) > 2 and all(part.isdigit() for part in parts[2].split(".")):
    risk_score += 4

risk_score += len(found_words) * 2

if len(url) > 75:
    risk_score += 2

if found_chars:
    risk_score += 2

risk_score = min(risk_score, 10)

if len(domain) > 30:
    risk_score += 2

# Final Result
print("\n" + "=" * 50)
print(f"🎯 RISK SCORE: {risk_score}/10")

if risk_score >= 6:
    print("🚨 VERDICT: HIGH RISK")
elif risk_score >= 3:
    print("⚠️ VERDICT: SUSPICIOUS")
else:
    print("✅ VERDICT: LOW RISK")

print("=" * 50)
