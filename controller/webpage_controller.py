from fastapi import APIRouter,Request,Form
from fastapi.responses import HTMLResponse,RedirectResponse
from config.utils import templates,sent_mail_now


controller=APIRouter()


@controller.get('/')
def get_initial_page(request:Request)->HTMLResponse:
    return templates.TemplateResponse("home.html",{"request":request,"page":"home"})

@controller.get('/about')
def get_about_page(request:Request)->HTMLResponse:
    return templates.TemplateResponse("about.html",{"request":request,"page":"about"})

@controller.get('/skills')
def get_skills_page(request:Request)->HTMLResponse:
    return templates.TemplateResponse("skills.html",{"request":request,"page":"skills"})

@controller.get('/projects')
def get_projects_page(request:Request)->HTMLResponse:
    return templates.TemplateResponse("projects.html",{"request":request,"page":"projects"})


@controller.get('/contact')
def get_contact_page(request:Request)->HTMLResponse:
    return templates.TemplateResponse("contact.html",{"request":request,"page":"contact"})

@controller.post("/sendMail")
def send_email(name:str=Form(...),email:str=Form(...),project_type:str=Form(...),message:str=Form(...)):
    sent_mail_now(name,email,project_type,message)
    return RedirectResponse(url="/?success=true",status_code=303)


