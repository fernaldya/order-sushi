class Session:
  def __init__(self, db_handler, id=None, created_at=None, updated_at=None):
    self.db_handler = db_handler
    self.id = id
    self.created_at = created_at
    self.updated_at = updated_at

  def all(self):
    data = self.db_handler.fetch_data('SELECT * FROM sessions')
    sessions = map(lambda x: Session(self.db_handler, x['id'], x['created_at'], x['updated_at']), data)
    return list(sessions)

  def find(self, id):
    session = self.db_handler.fetch_data('SELECT * FROM sessions WHERE id = {} LIMIT 1'.format(id))
    if len(session) == 1:
      data = session[0]
      return Session(self.db_handler, data['id'], data['created_at'], data['updated_at'])
    else:
      return None

  def serialize(self):
    return {
      'id': self.id,
      'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
      'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    }
