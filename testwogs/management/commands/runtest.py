from django.core.management.base import BaseCommand, CommandError

from testwogs import settings


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('testname', nargs='?', default='False', type=str)

    def handle(self, *args, **options):
        if options['testname'] == 'help':
            self.help_runtest()
            return
        if options['testname'] == 'showtests':
            self.show_all_tests()
            return
        if options['testname'] == 'runall':
            self.run_all_tests()
            return
        try:
            test_object = settings.TESTS_DICT[options['testname']]['class_name']
            test_object.run_test()
        except KeyError as key:
            print(f'Wrong test name - {key}!!!')
        self.stdout.write(self.style.SUCCESS('The program is completed!'))

    def run_all_tests(self):
        try:
            for name in settings.TESTS_DICT:
                test_object = settings.TESTS_DICT[name]['class_name']
                test_object.run_test()
        except KeyError as key:
            print(f'Wrong test name - {key}!!!')

    def show_all_tests(self):
        for test in settings.TESTS_DICT:
            print(test)

    def help_runtest(self):
        print('Command to show all name tests - manage.py runtest showtests')
        print('Command to run one test - manage.py runtest <test_name>')
        print('Command to run all tests - manage.py runtest runall ')