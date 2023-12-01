class Session:
  def __init__(self, db_handler, id=None, created_at=None, updated_at=None):
    self.db_handler = db_handler
    self.id = id
    self.created_at = created_at
    self.updated_at = updated_at

  def all(self):
    return self.db_handler.fetch_data('SELECT * FROM sessions')

  def find(self, id):
    session = self.db_handler.fetch_data('SELECT * FROM sessions WHERE id = {} LIMIT 1'.format(id))
    if len(session) == 1:
      return session[0]
    else:
      return None
