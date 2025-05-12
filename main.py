from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def root():
   return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message":"Welcome to about page"}

@app.get("/contact")
async def about():
    return {"message":"01611765966"}

@app.get("/home/{name}")
async def home(name: str = Path(..., min_length=3)):
    return {"name": name}