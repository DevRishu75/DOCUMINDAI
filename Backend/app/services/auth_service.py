from app.auth.password import hash_password,verify_password
from app.auth.jwt_token import create_access_token,create_refresh_token,decode_token
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.auth_request import RegisterRequest,LoginRequest

class AuthService:
    
    def register(self,data:RegisterRequest,db:Session):
        existing_user = (db.query(User).filter(User.email==data.email).first())

        if existing_user :
            return None

        #hash password
        hashed_password = hash_password(data.password)
        #create the user object
        user = User(
            email = data.email,
            password_hash = hashed_password
        )
        #add database to User table
        db.add(user)
        #commit the transaction
        db.commit()
        #refresh the table 
        db.refresh(user)
        return user

    def login(self,data:LoginRequest,db:Session):
        user = (db.query(User).filter(User.email==data.email).first())
        if not user:
            return None

        password_valid = verify_password(data.password,user.password_hash)

        if not password_valid:
            return None

        access_token = create_access_token(user.user_id)
        refresh_token = create_refresh_token(user.user_id)

        return {
            "access_token":access_token,
            "refresh_token":refresh_token
        }
    