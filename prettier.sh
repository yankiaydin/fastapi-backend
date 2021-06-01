#!/bin/bash

black app/run.py
black app/utils/const.py
black app/utils/db.py
black app/utils/db_object.py
black app/utils/db_functions.py
black app/utils/photo_upload.py
black app/utils/redis_object.py
black app/utils/security.py

black app/tests/all_tests.py
black app/tests/locust_test.py

black app/routes/v1.py
black app/routes/v2.py

black app/models/personel.py
