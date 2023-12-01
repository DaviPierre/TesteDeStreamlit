PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip3


run: install
	- $(PYTHON) teste.py

venv/bin/python3:
	- python3 -m venv venv

install: venv/bin/python3
	- $(PIP) install -r requirements.txt

commit:
	- git add .
	- git commit -m "Commit automático"
	- git push
