import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class =HTMLResponse)
def get_contacts():
    return """
        <h1> Buenas tardes LoL </h1>
        <p>Platzi Cursos</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
