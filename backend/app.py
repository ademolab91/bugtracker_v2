from fastapi import FastAPI
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from backend.users.routes import router as users_router
from backend.auth.routes import router as auth_router
from backend.tags import Tags
from backend.origins import origins


app = FastAPI(prefix="/api", tags=[Tags.api])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_router)
app.include_router(auth_router)
