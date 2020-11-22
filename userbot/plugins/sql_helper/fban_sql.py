try:
    from userbot.plugins.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String, UnicodeText


class Fban(BASE):
    __tablename__ = "fban"
    chat_id = Column(String(14), primary_key=True)
    fed_name = Column(UnicodeText)

    def __init__(self, chat_id, fed_name):
        self.chat_id = str(chat_id)
        self.fed_name = fed_name


Fban.__table__.create(checkfirst=True)


def get_flist():
    try:
        return SESSION.query(Fban).all()
    finally:
        SESSION.close()


def add_flist(chat_id, fed_name):
    adder = Fban(str(chat_id), fed_name)
    SESSION.add(adder)
    SESSION.commit()


def del_flist(chat_id):
    rem = SESSION.query(Fban).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def del_flist_all():
    SESSION.execute("""TRUNCATE TABLE fban""")
    SESSION.commit()
