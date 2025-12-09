from ultralytics import YOLO

model = YOLO("yolov9m.pt")

result = model.train(data = "dataset_custom.yaml",imgsz=640,batch = 8, epochs = 100,workers = 0 , device = 0)