import logging
from flask import Flask, request, jsonify
import numpy as np
import cv2
import os
import base64
from waitress import serve

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

confthres = 0.3
nmsthres = 0.1

# Define YOLO paths and load labels, config, and weights
yolo_path = "./yolo_tiny_configs"  # Specify your YOLO directory path
labelsPath = "coco.names"
cfgpath = "yolov3-tiny.cfg"
wpath = "yolov3-tiny.weights"

def get_labels(labels_path):
    lpath = os.path.sep.join([yolo_path, labels_path])
    LABELS = open(lpath).read().strip().split("\n")
    return LABELS

def get_weights(weights_path):
    weightsPath = os.path.sep.join([yolo_path, weights_path])
    return weightsPath

def get_config(config_path):
    configPath = os.path.sep.join([yolo_path, config_path])
    return configPath

LABELS = get_labels(labelsPath)
CFG = get_config(cfgpath)
Weights = get_weights(wpath)

def load_model(configpath, weightspath):
    net = cv2.dnn.readNetFromDarknet(configpath, weightspath)
    return net

nets = load_model(CFG, Weights)

def do_prediction(image, net, LABELS):
    (H, W) = image.shape[:2]
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)
    boxes = []
    confidences = []
    classIDs = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confthres:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confthres, nmsthres)
    predictions = []
    if len(idxs) > 0:
        for i in idxs.flatten():
            prediction = {
                "label": LABELS[classIDs[i]],
                "accuracy": confidences[i],
                "rectangle": {
                    "left": boxes[i][0],
                    "top": boxes[i][1],
                    "width": boxes[i][2],
                    "height": boxes[i][3]
                }
            }
            predictions.append(prediction)
    return predictions

@app.route('/predict', methods=['POST'])
def predict():
    try:
        req_data = request.get_json()
        images_data = req_data.get('images')
        all_predictions = []
        for image_data in images_data:
            image_base64 = image_data.get('image')
            image_bytes = base64.b64decode(image_base64)
            image_np = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
            predictions = do_prediction(image, nets, LABELS)
            all_predictions.append({"id": image_data.get("id"), "objects": predictions})
        logger.info("Predictions successfully generated.")
        return jsonify(all_predictions)
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)})

    
@app.route('/',methods=['GET'])
def fun():
    logger.info("Received GET request.")
    return jsonify({"success":"The webserver is running successfully"})

if __name__ == '__main__':
    logger.info("Starting the server...")
    serve(app,host='0.0.0.0',port=5000,threads=6)
