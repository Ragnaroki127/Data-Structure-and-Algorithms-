from functools import wraps

class Logit(object):
    def __init__(self, logfile):
        super().__init__()
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string)
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        print('Log file created')

@Logit('log.txt')
def my_func():
    pass

if __name__ == '__main__':
    my_func()
