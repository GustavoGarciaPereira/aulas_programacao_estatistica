from fastapi import FastAPI
from sympy import symbols, diff
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}


@app.get("/jonatan")
def main():
    return {"message": "Hello jonatan"}


@app.get("/derivada/{funcao}")
def main(funcao: str):
    x = symbols('x')

    funcao_para_derivar = funcao.replace("^", "**").replace(" ", "")
    print(funcao_para_derivar)
    print()
    return {
            "funcao": f"{funcao}",
            "funcao_derivada": f"{diff(funcao_para_derivar, x)}"
        }
@app.get("/items/")
async def read_items():
    html_content = """
        <!DOCTYPE html>
        <html>
        <body>

        <h1>The template Element</h1>

        <p>Click the button below to display the hidden content from the template element.</p>

        <button onclick="showContent()">Show hidden content</button>

        <template>
        <h2>Flower</h2>
        <img src="https://img.freepik.com/fotos-gratis/bela-foto-de-um-gatinho-branco-de-pelo-curto-britanico_181624-57681.jpg" width="214" height="204">
        </template>

        <script>
        function showContent() {
        let temp = document.getElementsByTagName("template")[0];
        let clon = temp.content.cloneNode(true);
        document.body.appendChild(clon);
        }
        </script>

        </body>
        </html>

    """
    return HTMLResponse(content=html_content, status_code=200)