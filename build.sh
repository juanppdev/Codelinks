python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
