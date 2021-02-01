#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoShorten.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()#test2#test4#test6#test8#test10#test12#test14#test16#test18#test20#test22#test24#test26#test28#test30#test32#test34#test36#test38#test40#test42#test44#test46#test48#test50#test52#test54#test56#test58#test60#test62#test64#test66#test68#test70#test72#test74#test76#test78#test80#test82#test84#test86#test88#test90#test92#test94#test96#test98#test100#test102#test104#test106#test108#test110#test112#test114#test116#test118#test120