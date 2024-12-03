.SILENT:

.PHONY: all format check
all: format check
	python -c "import glob, subprocess, sys; [subprocess.run([sys.executable, f]) for f in glob.glob('*.py')]"

format:
	ruff format *.py

check: format
	ruff check *.py
