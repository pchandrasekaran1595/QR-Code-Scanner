import os
import sys
import cv2
import webbrowser

READ_PATH = "Files"


def run():
    args_1: tuple = ("--code", "-c")

    name: str = None

    if args_1[0] in sys.argv: name = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: name = sys.argv[sys.argv.index(args_1[1]) + 1]

    assert name is not None, "Enter an argument for --code | -c"

    image = cv2.cvtColor(src=cv2.imread(os.path.join(READ_PATH, name), cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2RGB)

    qr_detector = cv2.QRCodeDetector()
    data, _, _ = qr_detector.detectAndDecode(image)

    webbrowser.open_new(data)