# Passwords: Make Guessing Hard

## Slide 1 — Why password strength matters

- Reused or predictable passwords let one breach put other accounts at risk.
- Attackers can try common passwords and patterns quickly, especially against stolen password hashes.
- A strength score is a clue, not a promise of safety.

**Speaker note:** This lesson uses synthetic examples only. Never paste a real password into a class demo or online checker.

## Slide 2 — Why weak passwords fail

- Names, dates, keyboard walks, and common substitutions are predictable.
- Adding a `1` or `!` to a familiar word often adds little protection.
- Reuse means one exposed password may unlock several services.

**Ask the audience:** Which would be easier to guess: `Summer2024!` or a random 16-character password?

## Slide 3 — How to build better passwords

- Use a password manager to create a long, random, unique password for each account.
- If you must memorize one, choose a long passphrase made from unrelated words.
- Length and uniqueness matter more than satisfying a symbol checklist.
- Never reuse your email password elsewhere.

## Slide 4 — What the checker can tell us

- Regex checks can report length, letters, digits, symbols, and obvious patterns.
- zxcvbn estimates how guessable a password may be and gives improvement hints.
- Neither approach knows whether a password was already exposed or reused.
- The demo runs locally and is designed not to print or save the entered value.

**Demonstration:** Run `python password_checker.py` with a made-up weak example, then a long, unique passphrase. Do not enter a personal password.

## Slide 5 — A safe offline cracking demonstration

- John the Ripper can compare candidate words to a password hash.
- The project includes 40 synthetic MD5 hashes and 40 matching wordlist examples.
- MD5 is intentionally outdated here to make the lesson quick; it is unsuitable for password storage.
- The exercise stays on the provided local sample. Never test against real accounts or unauthorized data.

**Takeaway:** Predictability makes guesses succeed. Unique, longer passwords and modern password hashing raise the cost of attacks.

## Slide 6 — Protect accounts beyond passwords

- Enable multifactor authentication.
- Use a password manager and secure its recovery options.
- Update a reused or exposed password immediately, including anywhere else it was reused.
- Be alert for phishing; a strong password cannot protect you if you hand it to an impostor.

**Closing message:** Long, unique, stored safely, and backed by MFA.
