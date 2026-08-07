from fastapi import APIRouter,HTTPException,status,Header
from pydantic import BaseModel,EmailStr
from fastapi.responses import JSONResponse
from supabase import create_client
from typing import Optional
from dotenv import load_dotenv
load_dotenv()
import os
SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_KEY=os.getenv("SUPABASE_KEY")

supabase=create_client(SUPABASE_URL,SUPABASE_KEY)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
class User(BaseModel):
    email:EmailStr
    password:str
@router.post("/signup",status_code=status.HTTP_201_CREATED)
def signup(user:User):
    if user.email.strip()=="" or user.password.strip()=="":
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )
    try:
        response=supabase.auth.sign_up(
            {
                "email":user.email,
                "password":user.password
            }
        )
        return {
            "message":"User registered successfully.",
            "user":response.user
        }
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={
                "error": "Signup failed"
            }
        )
@router.post("/login",status_code=status.HTTP_200_OK)
def login(user:User):
    if user.email.strip()=="" or user.password.strip()=="":
            raise HTTPException(
                status_code=400,
                detail="Email and password are required"
            )
    try:
         response=supabase.auth.sign_in_with_password({
              "email":user.email,
              "password":user.password
         })
         if response.session is None:
              return JSONResponse(
                  status_code=401,
                  content={
                      "error": "Invalid login credentials"
                  }
              )
         return{
              "access_token":response.session.access_token,
              "refresh_token": response.session.refresh_token,
              "token_type": "bearer"
         }
    except Exception:
         return JSONResponse(
          status_code=401,
          content={
              "error": "Invalid login credentials"
          }
        )

Profilerouter = APIRouter(
    prefix="",
    tags=["Profile"]
)
@Profilerouter.get("/public/info",status_code=status.HTTP_200_OK)
def publicInfo():
     return {
          "message":"Welcome stranger! This info is public."
     }
@Profilerouter.get("/protected/profile",status_code=status.HTTP_200_OK)
def protectedProfile( Authorization: Optional[str] = Header(None)):
     print("Authorization =", Authorization)
     if Authorization is None:
          return JSONResponse(
               status_code=401,
               content={"error":"Access token required"}
          )
     if not Authorization.startswith("Bearer "):
          return JSONResponse(
               status_code=401,
               content={
                    "error":"Access token required"
               }
          )
     token=Authorization.split(" ",1)[1].strip()

     if token=="":
          return JSONResponse(
               status_code=401,
               content={
                    "error":"Access token required"
               }
          )
     return{
          "message": "Protected route accessed successfully.",
          "access_token": token
     }
# @Profilerouter.get("/protected/profile")
# def protectedProfile(authorization: str = Header(default=None)):
#     print("Authorization =", authorization)

#     return {
#         "received": authorization
#     }