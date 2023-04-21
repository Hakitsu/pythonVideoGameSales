from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from videoGames.apiIA import prediction
from videoGames.forms import genreForm

from fastapi.staticfiles import StaticFiles


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    form = genreForm()
    return templates.TemplateResponse("index.html", {"request": request, "form": form})

@router.post("/", response_class=HTMLResponse)
async def predict(request: Request, platform: str, genre: str, year: str, publisher: str, na_sales: float, jp_sales: float, global_sales: float):
    result = prediction( {
            "platform": platform,
            "genre": genre,
            "year": year,
            "publisher": publisher,
            "na_sales": na_sales,
            "jp_sales": jp_sales,
            "global_sales": global_sales,
        })

    context = {
            "platform": platform,
            "genre": genre,
            "year": year,
            "publisher": publisher,
            "na_sales": na_sales,
            "jp_sales": jp_sales,
            "global_sales": global_sales,
            "result": result
        }

    return templates.TemplateResponse("predict.html", {"request": request, "context": context})


