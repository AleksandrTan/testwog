from django.core.management.base import BaseCommand, CommandError

from testwogs import settings


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('testname', nargs='?', default='False', type=str)

    def handle(self, *args, **options):
        try:
            test_object = settings.TESTS_DICT[options['testname']]['class_name']
            print(options)
            test_object.run_test()
        except KeyError as f:
            print('Wrong test name!!!', f)
        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))