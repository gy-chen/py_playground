from . import get_current_context, context


def set_name(name):
    ctx = get_current_context()
    ctx['name'] = name


def get_name():
    ctx = get_current_context()
    return ctx['name']


def main():
    with context():
        set_name('Monshin')
        with context():
            set_name('Tony')
            print('Name:', get_name())
        print('Name:', get_name())


if __name__ == '__main__':
    main()
