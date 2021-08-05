DRF Errors formatter
====================

This is a exception handlers error formating for Django REST Framework 
which allows you to format errors in all project.


Requirements
============

- Python (3.7+)
- Django (2.2+)
- djangorestframework (3.8+)

Installation
============

```
pip install drf-errors-formatter
```

Usage
=====
/home/thomas/Desktop/drf-errors-formatter/drf_handlers/formatter.py
Add formatter to DRF settings

```
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'drf_handlers.formatter.errors_exception_handler'
}

```


Authors
=======
2021, Thomas