import threading
from sqlalchemy import func, distinct, Column, String, Integer, UnicodeText
try:
    from userbot.plugins.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError


class Gallery(BASE):
    __tablename__ = "gallery"
    
    g_id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    foto = Column(UnicodeText, nullable=False)

    def __init__(self, foto):
        self.foto = foto

    def __repr__(self):
        return "<Gallery '%s' için %s>" % (self.g_id, self.foto)

    def __eq__(self, other):
        return bool(isinstance(other, Gallery)
            and self.foto == other.foto
            and self.g_id == other.g_id)


Gallery.__table__.create(checkfirst=True)

CMD_INSERTION_LOCK = threading.RLock()
TUM_GALLERY = SESSION.query(Gallery).all()

def ekle_foto(foto):
    with CMD_INSERTION_LOCK:
        try:
            SESSION.query(Gallery).filter(Gallery.foto == foto).delete()
        except:
            pass

        ekleme = Gallery(foto)
        SESSION.merge(ekleme)
        SESSION.commit()


def getir_foto():
    global TUM_GALLERY
    TUM_GALLERY = SESSION.query(Gallery).all()

def sil_foto(gid):
    try:
        SESSION.query(Gallery).filter(Gallery.g_id == gid).delete()
        SESSION.commit()
