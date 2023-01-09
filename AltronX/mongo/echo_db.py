import pymongo
from AltronX.mongo import AltUser


def is_echo(user_id, chat_id):
    try:
        return SESSION.query(ECHOSQL).get((str(user_id), str(chat_id)))
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_all_echos():
    try:
        return SESSION.query(ECHOSQL).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def addecho(user_id, chat_id):
    adder = ECHOSQL(str(user_id), str(chat_id))
    SESSION.add(adder)
    SESSION.commit()


def remove_echo(user_id, chat_id):
    note = SESSION.query(ECHOSQL).get((str(user_id), str(chat_id)))
    if note:
        SESSION.delete(note)
        SESSION.commit()
