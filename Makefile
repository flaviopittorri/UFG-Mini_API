.PHONY: install run test

install:
	python -m venv .venv
	.venv/Scripts/pip install --upgrade pip
	.venv/Scripts/pip install -r requirements.txt
	.venv/Scripts/pip install fastapi uvicorn[standard] pytest pytest-cov

run:
	.venv/Scripts/uvicorn.exe app.main:app --reload

test:
	.venv/Scripts/python.exe -m pytest --maxfail=5 --disable-warnings -v
