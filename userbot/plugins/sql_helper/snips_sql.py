from sqlalchemy import Column, LargeBinary, Numeric, UnicodeText

from userbot.plugins.sql_helper import BASE, SESSION


class Snips(BASE):
    __tablename__ = "snips"
    snip = Column(UnicodeText, primary_key=True)
    reply = Column(UnicodeText)
    snip_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        snip,
        reply,
        snip_type,
        media_id=None,
        media_access_hash=None,
        media_file_reference=None,
    ):
        self.snip = snip
        self.reply = reply
        self.snip_type = snip_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference


Snips.__table__.create(checkfirst=True)


def get_snips(keyword):
    try:
        return SESSION.query(Snips).get(keyword)
    except:
        return None
    finally:
        SESSION.close()


def get_all_snips():
    try:
        return SESSION.query(Snips).all()
    except:
        return None
    finally:
        SESSION.close()


def add_snip(keyword, reply, f_mesg_id):
    to_check = get_snips(keyword)
    if not to_check:
        adder = Note(keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Note).get(keyword)
    SESSION.delete(rem)
    SESSION.commit()
    adder = Note(keyword, reply, f_mesg_id)
    SESSION.add(adder)
    SESSION.commit()
    return False

def remove_snip(keyword):
    note = SESSION.query(Snips).filter(Snips.snip == keyword)
    if note:
        note.delete()
        SESSION.commit()
