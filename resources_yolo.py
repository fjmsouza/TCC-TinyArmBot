import gdown
import os

cwd = os.getcwd()

output = cwd + '/backend/controllers/yolo_crop/yolov4.weights'
id_drive = '1jzi1mk_7Z-mn_0xARVveiIBA0lJ14FtC'

a = gdown.download(id=id_drive, output=output, quiet=False)
