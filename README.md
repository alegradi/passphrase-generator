# Passphrase Generator App

I liked the passphrases you can generate at https://bitwarden.com/password-generator/ and wanted to make something similar. 

## Usage

1. Build the image
```
docker build -t <yourname>/passphrase-generator:1.0 .
```

2. Run it locally
```
docker run -d --rm --name pass-test -p 8080:5000  <yourname>/passphrase-generator:1.0
```

3. Test
```
curl http://localhost:8080
```

## Disclaimer

The words used for the passphrase generator have been inspected with `https://pypi.org/project/better-profanity/`. However some words might still be viewed as offensive. For any changes, please submit a pull request. 

Absolutely no warranty given. Use it at your own risk.
