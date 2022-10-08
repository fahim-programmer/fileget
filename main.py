import os
from pySmartDL import SmartDL


class filget:
    def __init__(self, argv):
        """ A high speed downloader class encapsulating
            a download library to make it streamline and
            some facilitating features to make it work
            smooth"""
        resource_url = None
        file_destination = None
        os.system('cls')
        if len(argv) < 1:
            print("No Arguments Provided")
            sys.exit()
        try:
            resource_url = argv[1]
        except Exception:
            print("No URL Provided")
        try:
            file_destination = argv[2]
        except Exception:
            print("No Destination Provided")
        try:
            if resource_url and file_destination is not None:
                self.initiate(resource_url, file_destination)
        except Exception:
            print("Failed to Download the file")

    def initiate(self, URL, DEST=None, PROG=True, CURRENT_DIR=True):
        """ Valid Parameters ::
        urls, dest=None, progress_bar=True, fix_urls=True, threads=5, timeout=5, logger=None, connect_default_logger=False, request_args=None, verify=True"""
        if CURRENT_DIR:
            DEST = os.getcwd() + '/' + DEST
        self.download_object = SmartDL(URL, dest=DEST, progress_bar=PROG)
        self.download_object.start()


if __name__ == '__main__':
    import sys
    filget(sys.argv)