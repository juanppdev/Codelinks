python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Solo inicializa si no existe el proyecto
if [ ! -f rxconfig.py ]; then
  reflex init
fi

reflex export
if [ -f frontend.zip ]; then
  rm -rf public
  unzip frontend.zip -d public
  rm -f frontend.zip
else
  echo "Error: frontend.zip no fue generado."
  exit 1
fi

deactivate
