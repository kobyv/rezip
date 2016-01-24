Microsoft Office (Open XML) and ODF files are ZIP compressed archives.
In order to allow efficient delta storage in git (or any other version control system),
the ZIP should be re-compressed in STORE mode.

Create and add to the repository a `.gitattributes` file as follows:
```
*.docx diff=textutil
*.docx filter=zipstore
*.xlsx filter=zipstore
```
The first line is optional, and allows diffing Microsoft word files under OS X.

Next, issue the following commands (creating entries in `.git/config`):
```
git config filter.zipstore.clean rezip.sh
git config diff.textutil.command "textutil -convert txt -stdout"
```

Copy `rezip.py` and `rezip.sh` to somewhere in your PATH.

The script is written in Python and should work with Python 2.7+ and Python 3.5+

For more information regarding GIT attributes, please refer to:
https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes

Note that for some reason, Python's stdout does not produce a binary stream when called by git. So a shell wrapper is used via a temporary file.

License: MIT
