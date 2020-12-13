import threading
from sqlalchemy import func, distinct, Column, String, UnicodeText
try:
    from userbot.plugins.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError


class messages(BASE):
    __tablename__ = "message"
    cmd = Column(UnicodeText, primary_key=True, nullable=False)
    message = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, cmd, message):
        self.cmd = cmd  # ensure string
        self.message = message

    def __repr__(self):
        return "<message '%s' for %s>" % (self.cmd, self.message)

    def __eq__(self, other):
        return bool(isinstance(other, messages)
                    and self.cmd == other.cmd
                    and self.message == other.message)


messages.__table__.create(checkfirst=True)

CMD_INSERTION_LOCK = threading.RLock()

def ekle_message(cmd, message):
    with CMD_INSERTION_LOCK:
        try:
            SESSION.query(messages).filter(messages.cmd == cmd).delete()
        except:
            pass

        cmd = messages(cmd, message)
        SESSION.merge(cmd)
        SESSION.commit()


def getir_message(komu):
    try:
        MESSAGE = SESSION.query(messages).filter(messages.cmd == komu).first()
        return MESSAGE.message
    except:
        return False
    

def sil_message(komu):
    try:
        SESSION.query(messages).filter(messages.cmd == komu).delete()
        SESSION.commit()
        except Exception as e:
        return e
    return True
