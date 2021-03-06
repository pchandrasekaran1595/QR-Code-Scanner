import os
import sys
import cv2
import webbrowser

READ_PATH = "Files"


def run():
    args: tuple = ("--code", "-c")

    name: str = None

    if args[0] in sys.argv: name = sys.argv[sys.argv.index(args[0]) + 1]
    if args[1] in sys.argv: name = sys.argv[sys.argv.index(args[1]) + 1]

    assert name is not None, "Enter an argument for --code | -c"

    image = cv2.cvtColor(src=cv2.imread(os.path.join(READ_PATH, name), cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2RGB)

    qr_detector = cv2.QRCodeDetector()
    data, _, _ = qr_detector.detectAndDecode(image)

    if data != "":
        webbrowser.open_new(data)
    else:
        print("\n" + 50*"*" + "\n")
        print("No data detected")
        print("\n" + 50*"*" + "\n")
