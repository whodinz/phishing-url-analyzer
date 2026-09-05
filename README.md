# 🔎 Phishing URL Analyzer

A beginner-friendly Python tool that analyzes URLs for common phishing indicators and generates a risk score.

## Features

- HTTPS detection
- IP address detection
- Suspicious keyword detection
- URL length analysis
- Suspicious character detection
- Risk score from 0–10
- Automatic risk verdict

## How It Works

The program checks a URL for several characteristics that can sometimes be associated with phishing attempts.

Each indicator contributes points to a risk score:

- No HTTPS → +2
- IP address used instead of a domain → +4
- Suspicious keyword → +2 each
- Unusually long URL → +2
- Suspicious character detected → +2

The final score is capped at 10.

## Example

```text
==================================================
        🔎 PHISHING URL ANALYZER
==================================================

Enter a URL to analyze: http://192.168.1.50/login

--------------------------------------------------
Analyzing: http://192.168.1.50/login
--------------------------------------------------

HTTPS:               ⚠️ No HTTPS detected
IP Address:          ⚠️ URL uses an IP address
Suspicious Keywords: ⚠️ Found login
URL Length:          ✅ Normal length
Suspicious Characters: ✅ None detected

==================================================
🎯 RISK SCORE: 8/10
🚨 VERDICT: HIGH RISK
==================================================
