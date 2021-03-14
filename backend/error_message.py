import sys

sys.path.insert(0, '.')


def py_error_message_to_babel():
    import error

    with open('error_messages.tmp', 'w+') as f:
        for key, value in error.ERR.__dict__.items():
            if not key.startswith('__'):
                f.write('gettext("{}")\n'.format(value[1]))

if __name__ == '__main__':
    py_error_message_to_babel()