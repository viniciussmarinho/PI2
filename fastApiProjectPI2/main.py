from fastapi import FastAPI
from src.py.routes.get.route import router_get
from src.py.routes.post.route import router_post

app = FastAPI()

app.include_router(router_get)
app.include_router(router_post)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
