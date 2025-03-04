# app.py
from nicegui import ui
from camera_control import take_photo

# Initialize global variables to hold camera state
camera = None
status = "Idle"

def start_capture(filename):
    global status
    if camera:
        try:
            file_path = take_photo(camera, filename)
            status = f"Image captured: {file_path}"
        except Exception as e:
            status = f"Capture failed: {e}"
    else:
        status = "Camera not initialized"

# Set up NiceGUI interface
with ui.card():
    ui.label("DSLR Camera Control").style('font-size: 24px; font-weight: bold;')

    # Input for filename and button to capture
    filename_input = ui.input("Filename", value="capture.jpg")
    ui.button("Capture Image", on_click=lambda: start_capture(filename_input.value))

    # Status display
    ui.label("Status:").style('font-size: 18px; font-weight: bold;')
    status_label = ui.label(status)

# Use a timer to update status label every second
def update_status():
    status_label.set_text(f"Status: {status}")

ui.timer(1.0, update_status)  # Runs every 1 second

# Start NiceGUI app
ui.run(port=5001)