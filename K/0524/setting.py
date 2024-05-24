class Setting:
    def __init__(self):
        self.config = {
            'right_pressed':False,
            'left_pressed': False,
            'ship_image_path':'images/ship.bmp',
            'alien_image_path': 'images/alien.bmp'
            
        }
    def get(self,key):
        return self.config[key]

    def set(self, key, value):
        self.config[key] = value