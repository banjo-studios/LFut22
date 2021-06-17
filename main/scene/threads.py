import threading, time

class loading_screen(threading.Thread):
    def __init__(self, timeleft):
        self.timeleft = timeleft

    def start(self) -> object:
        finished = False
        self.timeleft += 10
        time.sleep(0.25)
        if self.timeleft >= 200:
            finished = True

        return self.timeleft, finished
