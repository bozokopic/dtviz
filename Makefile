.POSIX:
.SUFFIXES:

PYTHON = python3

dist:
	$(PYTHON) -m mkwhl

install:
	$(PYTHON) -m pip install .

editable:
	$(PYTHON) -m pip install -e .

check:
	$(PYTHON) -m flake8 dtviz

requirements.pip.txt: pyproject.toml
	$(PYTHON) -m hat.json.convert $? | \
	jq -r '.project | .dependencies[], .["optional-dependencies"].dev[]' | \
	sort > $@

clean:
	rm -rf build
