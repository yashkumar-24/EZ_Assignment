from fastapi import FastAPI
from app.routes import ops, client

app = FastAPI()

app.include_router(ops.router, prefix="/ops", tags=["Operation User"])
app.include_router(client.router, prefix="/client", tags=["Client User"])

@app.on_event("startup")
def startup_event():
    print("App started!") 