from fastapi import FastAPI
from typing import Annotated
# from fastapi.middleware.cors import CORSMiddleware
from backend.users.routes import router as users_router
from backend.auth.routes import router as auth_router
from backend.tags import Tags


app = FastAPI(prefix="/api", tags=[Tags.api])
app.include_router(users_router)
app.include_router(auth_router)