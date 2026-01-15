from fastapi import FastAPI

app = FastAPI(title="python-tester", version="0.1.0")


@app.get("/")
def root():
    return {"status": "ok", "message": "codespace proxy test"}


@app.get("/health")
def health():
    return {"health": "up"}
