# camera_control.py
import gphoto2 as gp
import time

def init_camera():
    """Initialize the camera."""
    camera = gp.Camera()
    camera.init()
    return camera

def capture_image(camera, filename="capture.jpg"):
    """Capture an image and save it to the specified filename."""
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    target_path = f"/path/to/save/{filename}"
    camera_file = camera.file_get(
        file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    camera_file.save(target_path)
    return target_path

def release_camera(camera):
    """Release the camera."""
    camera.exit()
