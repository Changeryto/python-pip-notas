# Este es un repositorio con el objetivo de practicar PIP y entornos virtuales.

Las notas de cada clase se pueden observar a continuación.

## .gitignore adecuado

Puede obtenerse se https://www.toptal.com/developers/gitignore
Siempre considerando los OS que podrían usarse en cualquier colaborador del proyecto.

## Game Project
Comandos para correr el juego.

```sh
cd game
python main.py
```

## ¿Qué es pip?

Dentro del ecosistema se pueden crear grandes bibliotecas ya creadas, los paquetes están en el gestor de paquetes de python (pip).

Toda la familia de paquetes se encuentran en pypi.org

La forma de instalar paquetes desde pip se hace con.

pip install [nombre_de_biblioteca]

## Conocer las bibliotecas en el entorno global de python.

```sh
pip freeze
```

## Crear entorno virtual

```sh
python -m venv {nombre}
```

Usualmente nombre es solo env

```sh
# Activar el ambiente
source env/bin/activate

# Desactivar el ambiente
deactivate
```

Al principio no habrá paquetes instalados en el nuevo entorno virtual.

# requirements.txt
Este archivo gestiona las dependencias y los archivos que requiere el proyecto.

En general se convierte pip freeze a un requirements.txt

Se crea con 

```sh
pip freeze > requirements.txt
```

Y para instalar las dependencias.

```sh
pip install requirements.txt
```

# App Proyect

Instrucciones para levantar el proyecto.

```sh
git clone xxx
cd app
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```

# Solicitudes HTTP con request

```python
import request

r = requests.get("https://api.escuelajs.co/api/v1/categories")
```

# Lanzar servidor con Uvicorn

```sh
uvicorn main:app --reload
```
