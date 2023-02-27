from picamera import PiCamera

camera = PiCamera()

camera.start_preview()
camera.capture("./test-imgs/test_quality.jpg",quality=3)
camera.stop_preview()
