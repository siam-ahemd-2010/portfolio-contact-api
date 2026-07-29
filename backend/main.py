from fastapi import FastAPI
from pydantic import BaseModel

from db import engine
from models import Base
from email_sender import send_email, send_auto_reply
from db import SessionLocal
from models import Contact
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5501",
        "http://localhost:5501",
        "https://siyam-bay.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


class ContactRequest(BaseModel):
    name: str
    email: str
    subject: str
    message: str


@app.get("/")
def home():
    return {
        "message": "Portfolio Contact API Running Successfully"
    }


@app.post("/contact")
def receive_contact(data: ContactRequest):

    db = SessionLocal()

    new_contact = Contact(
        name=data.name,
        email=data.email,
        subject=data.subject,
        message=data.message
    )

    db.add(new_contact)

    db.commit()

    db.refresh(new_contact)

    db.close()

    # send_email(
    #       data.name,
    #       data.email,
    #       data.subject,
    #       data.message
    #  )

    # send_auto_reply(
    #       data.email,
    #       data.name
    #  )

    return {
        "success": True,
        "message": "Message saved successfully."
    }