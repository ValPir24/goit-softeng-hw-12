from fastapi import FastAPI, Depends
from app.routers import contacts, users
from app.dependencies import get_db
from app.database import async_create_all, close_db_session
from app import auth

app = FastAPI()

# Запуск створення таблиць при старті додатку
@app.on_event("startup")
async def startup_event():
    await async_create_all()

# Закриття сесії бази даних при зупинці додатку
@app.on_event("shutdown")
async def shutdown_event():
    await close_db_session()

app.include_router(auth.router, prefix="/auth", tags=["auth"], dependencies=[Depends(get_db)])
app.include_router(users.router, prefix="/users", tags=["users"], dependencies=[Depends(get_db)])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"], dependencies=[Depends(get_db)])
