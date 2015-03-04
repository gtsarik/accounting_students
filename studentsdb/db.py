DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': '123',
        'NAME': 'accounting_students_db',
    }
}
