# create a contract (skeleton) that must be implemented in the class that inherits it

from abc import ABC, abstractmethod


class Camera(ABC):
    @abstractmethod
    def set_lens_size(self, size):
        pass


class Professional_camera(Camera, ABC):
    def set_lens_size(self, size):
        print(f"Changing lens size to {size}")


professionalCamera = Professional_camera()
professionalCamera.set_lens_size(5)