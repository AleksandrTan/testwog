from django.core.management.base import BaseCommand, CommandError

import testwogs.settings as st
from testwogs.testsdir.logintest import LoginTest


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print(st.a)
        g = LoginTest()
        print(g.getbaseurl())
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % st.a))