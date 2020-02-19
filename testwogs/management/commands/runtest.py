from django.core.management.base import BaseCommand, CommandError

from testwogs import settings


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('testname', type=str)

    def handle(self, *args, **options):
        try:
            test_object = settings.tests_dict[options['testname']]['class_name']
            print(test_object.get_request_url())
            test_object.run_test()
        except KeyError:
            print('Wrong test name!!!')
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % settings.a))