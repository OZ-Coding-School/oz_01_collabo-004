import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from MySQLdb import OperationalError as MysqlOpError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB Connection...")

        is_db_connected = None

        while not is_db_connected:
            try:
                is_db_connected = connections["default"]
            except (MysqlOpError, OperationalError):
                self.stdout.write("Connection Trying...")

        self.stdout.write(self.style.SUCCESS("MySQL Connection Successful"))
