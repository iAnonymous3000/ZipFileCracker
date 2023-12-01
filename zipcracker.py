import zipfile
import threading 
import logging
import itertools
import queue
import time

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class ZipCracker:
    def __init__(self, zip_file, charset, max_length):
        self.zip_file = zip_file
        self.charset = charset
        self.max_length = max_length
        self.stop_event = threading.Event()
        
        self.passwords_queue = queue.Queue() 
        self.found_queue = queue.Queue()
        
        self.generate_passwords()
        
    def generate_passwords(self):
        for length in range(1, self.max_length+1):
            for password in itertools.product(self.charset, repeat=length):
                self.passwords_queue.put(''.join(password))
                
    def attempt_password(self):
        while not self.stop_event.is_set():
            try:
                password = self.passwords_queue.get(timeout=0.5)
                with zipfile.ZipFile(self.zip_file) as zf:
                    zf.extractall(pwd=password.encode())
                self.found_queue.put(password)
                self.stop_event.set()
                return
            except queue.Empty:  
                continue
            except RuntimeError:
                continue
            
    def print_status(self):
        start = time.time()
        while not self.stop_event.is_set():
            elapsed = time.time() - start
            logging.info(f"Elapsed Time: {elapsed:0.2f}s")
            time.sleep(2)
            
    def run(self):
        threads = [threading.Thread(target=self.attempt_password) for _ in range(8)]
        status_thread = threading.Thread(target=self.print_status)
        
        for thread in threads:
            thread.start()
        status_thread.start()
        
        for thread in threads:
            thread.join()
            
        if not self.found_queue.empty():
            password = self.found_queue.get()
            logging.info(f"Password found: {password}")
        else:
            logging.info("Password not found")
            
        status_thread.join()
            
if __name__ == "__main__":
    cracker = ZipCracker("encrypted.zip", "01234abc", 4)  
    cracker.run()
