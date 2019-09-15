# CryptonDie

<p align="center">
  <h3 align="center">CryptonDie</h3>
  <p align="center">CryptonDie is a ransomware developed for study purposes.</p>

  <p align="center">
    <a href="https://twitter.com/zer0dx">
      <img src="https://img.shields.io/badge/twitter-@zer0dxx-blue.svg">
    </a>
  </p>
</p>

<hr>

### Options

```text
    --key       key used to encrypt and decrypt files - key size (16 bytes)
    --dir       Home directory for the attack, default is /
    --encrypt   Encrypt all files
    --decrypt   Decrypt all files
    --verbose   Active verbose mode, default is False

Example:
    python3 cryptondie.py --dir /var/www/ --key 0123456789abcdef --encrypt --verbose

```

### Running in Docker

```bash
docker build -t cryptondie .
docker run -it cryptondie /bin/bash
python cryptondie.py --dir /etc --key 0123456789abcdef --encrypt --verbose
```

### which encryption is implemented?

```text
Advanced Encryption Standard
```

### Contact

```text
[+] Telegram:   @zer0dx
[+] Github:     https://github.com/zer0dx
[+] Twitter:    https://twitter.com/zer0dxx
[+] Blog:       https://zer0dx.github.io
```

<p align="center">
  <p align="center">chaos is order yet undeciphered.</p>
</p>