
from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


SessionFactory = sessionmaker()
Session = scoped_session(SessionFactory)