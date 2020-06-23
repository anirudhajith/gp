# gp
### Generate Password: Personal multi-platform password generation scheme

This is an implementation of a password generation scheme I thought of which satisfies the following properties:
1) The generation procedure is completely deterministic.
2) Passwords on two distinct platforms are as different from each other as possible. Knowledge of one password does not compromise others.
3) Passwords generated are far removed from dictionary words.
4) If lost, passwords generated this way are easily re-obtainable.
5) In the event that a password is compromised, it is easily replaceable without any loss in the degree of security offered by the replacement.

#### Additional features:
1) Passwords of reasonable length [5, 64] are generatable. By default, passwords of length 16 are generated.
2) Passwords generated are compliant to requirements for passwords on most platforms.
* at least one lowercase character
* at least one uppercase character
* at least one special character
* at least one digit
3) Knowledge of the scheme of generation does not diminish the security of passwords generated.

#### Usage:
* To generate a password for a single platform, use
```
python3 gp.py PLATFORM_NAME
```
* To generate passwords for multiple platforms, list them in a plaintext `FILE` with each platform on a new line and run
```
python3 gp.py --list FILE
```
* To create a password of a nondefault length, use the optional argument `--length LENGTH`.

You will be asked to provide your secret string in each of these cases. 

**Do not divulge your secret string to anyone. If you do, a person with knowledge of the scheme can recover all of your passwords.**

It is recommended that you use a password manager in addition to this scheme since the generated passwords may be difficult to remember.