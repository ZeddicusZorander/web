CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/',
    'args': (
        '--bind=127.0.0.1:8000',
        '--workers=16',
        '--timeout=60',
        'AppModule.module',
    ),
}