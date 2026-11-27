# Password Strength Checker

A small Python command-line tool for learning about password strength. It checks a few visible characteristics with regular expressions and, when installed, uses `zxcvbn` for a more useful estimate that accounts for common words and patterns.

## Run it

Python 3.9 or newer is recommended.

```text
python -m pip install -r requirements.txt
python password_checker.py
```

The password prompt is hidden. The program evaluates the value on your machine, does not print or save it, and does not make network requests. Use a newly invented example rather than a password you currently use. `zxcvbn` is optional at runtime: if it is missing, the program reports its basic checklist and explains how to enable the estimator.

The checklist is not a policy that every password must satisfy. A long, unique passphrase can be strong without symbols; a short password with mixed character types can still be easy to guess. The zxcvbn score is an estimate, not a guarantee or a measurement of account security.

## What it checks

- Length targets of 12 and 16 characters.
- Lowercase and uppercase letters, digits, and symbols/non-ASCII characters.
- Obvious repetition and common password words or sequences.
- zxcvbn score and suggestions, when available.

## Offline John the Ripper classroom demonstration

This optional exercise cracks only a deliberately weak, synthetic MD5 hash included for the demo. It is an obsolete hash format and must never be used to store real passwords. Run only in a local lab with this provided sample; do not use these techniques against accounts or hashes you do not own or have permission to test.

Install John the Ripper from its official distribution for your operating system. The included `demo-wordlist.txt` contains 40 synthetic weak-password examples, and `demo_hashes.txt` contains one matching MD5 hash for each entry. From this folder, run:

```text
john --format=Raw-MD5 --wordlist=demo-wordlist.txt demo_hashes.txt
john --show --format=Raw-MD5 demo_hashes.txt
```

The hash file uses John’s `username:hash` format. The first command tries the 40 candidate words against the offline hashes; `--show` displays the recovered demo values. For a bounded brute-force exercise, use a separate throwaway hash for a short, known lab string and cap the search length, for example:

The completed dictionary-demo result is recorded in [demo-results.md](demo-results.md).

```text
john --format=Raw-MD5 --incremental=LowerNum --min-length=1 --max-length=4 demo_short_hash.txt
```

For a reproducible throwaway hash of the four-character classroom string `cat7`, create the input with:

```text
python -c "import hashlib; print(hashlib.md5(b'cat7').hexdigest() + ':classroom-short-demo')" > demo_short_hash.txt
```

Then run the bounded command above. A brute-force search grows rapidly with length and character-set size; do not remove the cap or point the command at real credential data. Delete the temporary lab file after class.

## Secure password habits

Use a password manager to create and store a different, random password for every account. Prefer long, unique passwords or passphrases. Turn on multifactor authentication, especially for email and financial accounts. Never share passwords, and change a password promptly if a service reports a breach. See [presentation.md](presentation.md) for a short classroom presentation outline.
