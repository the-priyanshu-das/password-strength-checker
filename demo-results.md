# Offline cracking demo results

**Scope:** Local classroom example using only the provided synthetic hash and wordlist. No real password or account data was used.

**Hash type:** Raw MD5 (intentionally obsolete for this demonstration)

**Commands:**

```text
john --format=Raw-MD5 --wordlist=demo-wordlist.txt demo_hashes.txt
john --show --format=Raw-MD5 demo_hashes.txt
```

**Initial observed result:** Before the sample set was expanded, John loaded the `password123` hash, found it in the wordlist, and reported one hash cracked. This illustrates why predictable passwords are risky when an attacker obtains a password hash. The bundled demo now contains 40 synthetic wordlist entries and 40 matching hashes; run the commands above to demonstrate the expanded set. This does not represent the speed or difficulty of attacking a modern service, which should use a suitable password hashing scheme and other defenses.

The demo ran with John the Ripper's official Windows release. John was used from a temporary project-local folder; it was not installed system-wide.
