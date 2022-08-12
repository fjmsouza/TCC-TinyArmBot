import cv2
import os
os.chdir('../')
cwd = os.getcwd()


class Crop:
    @staticmethod
    def get_cropped_frames(frame):
        config_path = cwd + '/backend/controllers/yolo_crop/yolov4.cfg'
        weights_path = cwd + '/backend/controllers/yolo_crop/yolov4.weights'
        yolo_net = cv2.dnn_DetectionModel(config_path, weights_path)
        yolo_net.setInputSize(704, 704)
        yolo_net.setInputScale(1.0 / 255)
        yolo_net.setInputSwapRB(True)
        frame_titulo = None
        frame_votos = None

        with open(cwd + '/backend/controllers/yolo_crop/obj.names') as f:
            names = f.read().rstrip('\n').split('\n')
        x_ini = 0
        x_fin = 0
        y_ini = 0
        y_fin = 0

        classes, confidences, boxes = yolo_net.detect(frame, confThreshold=0.1, nmsThreshold=0.4)
        copy = frame.copy()

        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            label = '%.2f' % confidence
            label = '%s: %s' % (names[classId], label)
            label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 5)
            left, top, width, height = box
            top = max(top, label_size[1])
            cv2.rectangle(frame, box, color=(0, 255, 0), thickness=3)
            cv2.rectangle(frame, (left, top - label_size[1]), (left + label_size[0], top + base_line), (255, 255, 255),
                          cv2.FILLED)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (20, 20, 20))

            x_ini = left
            x_fin = left + width
            y_ini = top
            y_fin = top + height

            cropped_img = copy[y_ini:y_fin, x_ini:x_fin]

            if classId == 0:
                frame_titulo = cropped_img
            else:
                frame_votos = cropped_img

        return frame_titulo, frame_votos
