### Clone repo
```bash
git clone git@github.com:sebastienpro/ch-ales.git
cd chales
```

### install weasyprint dependencies
https://weasyprint.readthedocs.io/en/latest/install.html#macos

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install python3 cairo pango gdk-pixbuf libffi 
```

### Create venv
```bash
python3 -m venv venv

source ven/bin/activate
```

### install pip requirements
```bash
pip install -r requirements.txt
```

### launch develop service
```
./main.py 
```

### See result in browser
http://127.0.0.1:5000
or
http://127.0.0.1:5000/test.pdf