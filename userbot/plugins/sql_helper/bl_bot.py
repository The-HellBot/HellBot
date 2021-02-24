from sqlalchemy import Column, String

from . import BASE, SESSION


class Blockedid(BASE):
    __tablename__ = "blockedid"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Blockedid.__table__.create(checkfirst=True)


def add_in_db(chat_id: int):
    id_user = Blockedid(str(chat_id))
    SESSION.add(id_user)
    SESSION.commit()


def get_all_ids():
    nibbaid = SESSION.query(Blockedid).all()
    SESSION.close()
    return nibbaid


def is_id_added(chat_id):
    try:
        return SESSION.query(Blockedid).filter(Blockedid.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()


def removeid(chat_id):
    nibbanoob = SESSION.query(Blockedid).get(str(chat_id))
    if nibbanoob:
        SESSION.delete(nibbanoob)
        SESSION.commit()
