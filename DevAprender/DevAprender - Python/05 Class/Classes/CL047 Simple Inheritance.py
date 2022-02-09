# heritage
class camera(object):
    # The class will inherit object functions
    def __init__(self, brand, megapixels):
        self.brand = brand
        self.megapixels = megapixels

    def take_picture(self):
        print(f"Photo taken with {self.brand} camera with the quality of {self.megapixels} megapixels.")


# Looks like import


class cell_camera(camera):
    # This class will inherit the class camera
    def __init__(self, brand, megapixels, cameras):
        super().__init__(brand, megapixels)
        self.cameras = cameras

    def apply_effect(self, effect):
        print(f"Applying effect {effect}")

    def take_picture(self, which_camera):
        print(f"Photo taken with {self.brand} camera with the quality of {self.megapixels} megapixels. (Using the camera {which_camera})")


cellCamera = cell_camera("Sony", "25mp", "4")
cellCamera.apply_effect("Blue")
cellCamera.take_picture(2)


# I can make with that a new class also inherit 'camera'

class security_camera(camera):
    def __init__(self, brand, megapixels, recording_hours):
        super(security_camera, self).__init__(brand, megapixels)
        self.recording_hours = recording_hours

    def rotate_camera(self, direction):
        print(f"Rotating to {direction}")


securityCamera = security_camera("Sony", "5mp", 10)
securityCamera.rotate_camera("Right")


# Doubt

print(issubclass(cell_camera, camera))
print(issubclass(security_camera, camera))

