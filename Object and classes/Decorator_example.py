def is_user_authenticated():
    return False


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print('User authenticated!')
            return fn(*args, **kwargs)
        else:
            print('User is NOT authenticated!')
    return wrapper


@check_user_auth
def do_sensitive_job():
    print('Results of some tasks')


try:
    do_sensitive_job()
except Exception as e:
    print(e)
