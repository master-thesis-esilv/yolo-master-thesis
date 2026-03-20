from ultralytics import YOLO
model = YOLO("yolo11n-pose.pt") # 'n' is the Nano version, very light!
results = model.track(source="inputs/judo.mp4", save=True, tracker="botsort.yaml")