"""
Django command to wait for database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

"""Error Django throws when db is not ready"""
from django.db.utils import OperationalError  # noqa: E402
from django.core.management.base import BaseCommand  # noqa: E402


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('waiting for db...')
        """assume db is not up until we know for sure"""
        db_up = False
        """while db_up is false well do the try/catch and tell us it is not
        ready"""
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                """if we get Psycoppg2Error or Operational error print to
                screen"""
                self.stdout.write('db unavail, waiting...')
                time.sleep(1)

        """self.style.SUCCESS gives a nice green output"""
        self.stdout.write(self.style.SUCCESS('db up and avail'))
