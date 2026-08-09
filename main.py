from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, pgs, reviews

app = FastAPI(title="PG Review API")
app.include_router(auth.router)
app.include_router(pgs.router)
app.include_router(reviews.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}