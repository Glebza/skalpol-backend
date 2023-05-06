from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:3000", # Replace this with the address of your frontend app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/diagrams/{id}")
async def get_diagram(id: int):
    # Your logic to retrieve the diagram with the given id

    #diagram = {"id": 1, "title": "Example Diagram", "author": "Gleb S.", "elements": [{"id": 1, "elementType": "filter"}]}
    diagram = {"id": 1, "title": "Example Diagram", "author": "Gleb S.", "elements": []}
    return diagram


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
