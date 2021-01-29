import self as self

class Adjacency(object):
    def __init__(self, object_id, priority, distance, tier, attempts, hosr):
        self.object_Id = object_id
        self.priority = priority
        self.distance = distance
        self.tier = tier
        self.attempts = attempts
        self.hosr = hosr
