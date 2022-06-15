from datetime import datetime
import threading
import shutil

class log:
    def __init__(self):
        log = open('personal_account_python_log.txt', 'w')
        log.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' - Log created')
        log.close()
        self.log_backup()
    def log_get():
        log = open('personal_account_python_log.txt', 'r')
        log_lines = log.read().splitlines()
        log.close()
        return log_lines
    def log_new(action):
        log = open('personal_account_python_log.txt', 'a')
        log.write('\n' + datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' - ' + action)
        log.close()
    def log_backup(self):
        shutil.copyfile('personal_account_python_log.txt', 'personal_account_python_log_backup.txt')
        start_time = threading.Timer(3600, self.log_backup)
        start_time.start()