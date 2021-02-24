from sqlalchemy import Column, Integer, String

from . import BASE, SESSION


class Users(BASE):
    """ Table to store the received messages """

    __tablename__ = "users"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14))
    um_id = Column(Integer)

    def __init__(self, message_id, chat_id, um_id):
        self.message_id = message_id
        self.chat_id = str(chat_id)  # ensure string
        self.um_id = um_id

    def __repr__(self):
        return "<User %s>" % self.chat_id


Users.__table__.create(checkfirst=True)


def add_id_in_db(message_id: int, chat_id: int, um_id: int):
    __user = Users(message_id, str(chat_id), um_id)
    SESSION.add(__user)
    SESSION.commit()


def its_userid(message_id: int):
    try:
        s__ = SESSION.query(Users).get(str(message_id))
        return int(s__.chat_id), s__.um_id
    finally:
        SESSION.close()
