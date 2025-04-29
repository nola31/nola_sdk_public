import time
import threading

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
        if self.running:
            self.running = False
            if self.thread:
                self.thread.join()

    def _pulse_loop(self):
        while self.running:
            print("[Pulse] Прошел еще один интервал.")
            time.sleep(self.interval)

# При запуске напрямую
if __name__ == "__main__":
    pulse = NolaPulse(interval_seconds=60)
    pulse.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pulse.stop()