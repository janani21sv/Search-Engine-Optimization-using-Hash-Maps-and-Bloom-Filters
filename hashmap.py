class HashMap:
    def __init__(self):
        self.map = {}

    def set(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key, [])

    def remove(self, key):
        if key in self.map:
            del self.map[key]
