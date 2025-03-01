# app.py
from flask import Flask, request
from nicegui import ui, app
from camera_control import init_camera, capture_image, release_camera

# Initialize Flask app
flask_app = Flask(__name__)

# Initialize global variables to hold camera state
camera = None
status = "Idle"

@flask_app.route('/status')
def get_status():
    """Route to check camera status."""
    return {"status": status}

def initialize_camera():
    global camera, status
    try:
        camera = init_camera()
        status = "Camera initialized"
    except Exception as e:
        status = f"Initialization failed: {e}"

def start_capture(filename):
    global status
    if camera:
        try:
            file_path = capture_image(camera, filename)
            status = f"Image captured: {file_path}"
        except Exception as e:
            status = f"Capture failed: {e}"
    else:
        status = "Camera not initialized"

def release():
    global camera, status
    if camera:
        try:
            release_camera(camera)
            status = "Camera released"
            camera = None
        except Exception as e:
            status = f"Release failed: {e}"
    else:
        status = "Camera not initialized"

# Set up NiceGUI interface
@app.get('/')
async def gui():
    with ui.card():
        ui.label("DSLR Camera Control").style('font-size: 24px; font-weight: bold;')

        # Button to initialize the camera
        ui.button("Initialize Camera", on_click=initialize_camera)

        # Input for filename and button to capture
        filename_input = ui.input("Filename", value="capture.jpg")
        ui.button("Capture Image", on_click=lambda: start_capture(filename_input.value))

        # Button to release the camera
        ui.button("Release Camera", on_click=release)

        # Status display
        ui.label("Status:").style('font-size: 18px; font-weight: bold;')
        status_label = ui.label(status)

        # Update status label
        async def update_status():
            while True:
                status_label.set_text(f"Status: {status}")
                await ui.sleep(1)  # Poll every second

        # Run the status update in a background task
        ui.run_task(update_status)

# Run the Flask app with NiceGUI
if __name__ == '__main__':
    app.run_with(flask_app, port=5000)
