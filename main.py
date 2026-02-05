from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from controller.webpage_controller import controller
app=FastAPI()
app.mount("/assets",StaticFiles(directory="assets"),name="assets")
app.include_router(controller)
if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)