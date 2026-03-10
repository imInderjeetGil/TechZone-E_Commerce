from fastapi import FastAPI
from db.session import engine
from models import user,product
from db.base import Base
from api import product,auth
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Demo of FastAPI Basics")

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )

@app.get("/products-ui")
def products_ui(request: Request):
    return templates.TemplateResponse(
        "products.html",
        {"request": request}
    )
    
@app.get("/add-product-ui")
def add_product_ui(request:Request):
    return templates.TemplateResponse(
        "add_products.html",
        {"request": request}
    )    

@app.get("/edit-product-ui")
def edit_product_ui(request: Request):
    return templates.TemplateResponse(
        "edit_product.html",
        {"request": request}
    )

@app.get("/login-ui")
def login_ui(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

app.include_router(product.router)
app.include_router(auth.router)
