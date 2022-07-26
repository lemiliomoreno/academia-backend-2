from sqlalchemy.orm import Session

from models.users import User, CreateUser


def create_user(db: Session, user: CreateUser):
    db_user = User(
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    return db_user


def get_all_users(db: Session):
    db_users = db.query(User).all()
    return db_users
