from fastapi import FastAPI, HTTPException, Cookie, Response
from pydantic import BaseModel
from typing import Dict, List,Annotated,Optional
from datetime import datetime, timedelta,timezone


app = FastAPI()

class Auth(BaseModel):
    username : str
    password : str



@app.post("/login/")
async def login(auth : Auth , response : Response):
    if auth.username == "Admin" and auth.password == "admin":
        expires = datetime.now(timezone.utc) + timedelta(days=1)
        response.set_cookie(key="auth_token", value="secure_token_value", expires=expires, httponly=True, secure=True)
        return {"Msg" : "Login Successfully"}
    else:
        raise HTTPException(status_code=401, detail="Invalid User")
    

class Toy_Param(BaseModel):
    number :int
    name:str
    desc : Optional[str] = None
    has_discount: Optional[bool] = None

    
toy_DB : List[Toy_Param] = []

@app.get("/store/")
async def toy_list(my_cookie:str = Cookie(None)):
    if my_cookie:
        return toy_DB
    else:
        raise HTTPException(status_code=401,detail="NOt Logined !")


@app.post("/store/")
async def new_toy(param : Toy_Param, my_cookie: str = Cookie(None)):
    if my_cookie :     
        toy_DB.append(param)
        return {"Msg" : "Save Successfull"}
    else:
        raise HTTPException(status_code=401,detail="NOt Logined !")

@app.put("/store/{number}")
async def retoy(number: int, param: Toy_Param, fall: Optional[str] = None,my_cookie: str = Cookie(None)):
    if my_cookie:
        for i, db in enumerate(toy_DB):
            
            if db.number == number:
                toy_DB[i] = param
                return {"Msg" : "Update Successfull"}
        raise HTTPException(status_code=404,detail="number not found !")
    else:
        raise HTTPException(status_code=401,detail="NOt Logined !")
