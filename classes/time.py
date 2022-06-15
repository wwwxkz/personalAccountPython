from datetime import datetime
import shutil

class log:
    def __init__(self):
        log = open('personal_account_python_log.txt', 'w')
        date = datetime.now()
        log.write(date.strftime('%m/%d/%Y, %H:%M:%S') + ' - Log created')
        log.close()
    def log_get():
        log = open('personal_account_python_log.txt', 'r')
        log_lines = log.read().splitlines()
        log.close()
        return log_lines
    def log_new(action):
        log = open('personal_account_python_log.txt', 'a')
        date = datetime.now()
        log.write('\n' + date.strftime('%m/%d/%Y, %H:%M:%S') + ' - ' + action)
        log.close()
    def log_backup(self):
        shutil.copyfile('personal_account_python_log.txt', 'personal_account_python_log_backup.txt')