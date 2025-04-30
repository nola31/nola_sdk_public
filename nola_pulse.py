import time
import threading
from datetime import datetime

class NolaPulse:
    def __init__(self, interval_seconds=60):
        self.interval = interval_seconds
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._pulse_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _pulse_loop(self):
        while self.running:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[Pulse] {timestamp} — интервал прошёл.")
            time.sleep(self.interval)