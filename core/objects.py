import uuid

class Point:
    def __init__(self, x, y):
        # x, y in logical space [-1, 1]
        self.x = x
        self.y = y
        self.id = str(uuid.uuid4())

class Line:
    def __init__(self, p1_id, p2_id):
        self.p1_id = p1_id
        self.p2_id = p2_id
        self.id = str(uuid.uuid4())

class Triangle:
    def __init__(self, p1_id, p2_id, p3_id):
        self.p1_id = p1_id
        self.p2_id = p2_id
        self.p3_id = p3_id
        self.id = str(uuid.uuid4())
