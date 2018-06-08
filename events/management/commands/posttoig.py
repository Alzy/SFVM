from django.core.management.base import BaseCommand, CommandError
from events.models import Event
import datetime
import os
from InstagramAPI import InstagramAPI


class Command(BaseCommand):
    help = 'Posts tomorrow\'s events to sfvm.la\'s instagram account'

    def handle(self, *args, **options):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        # update DATABASE_NAME to use \$ instead of $ else commands wont work
        os.putenv(
            "DATABASE_NAME",
            "alzy\\$sfvm"
        )

        try:
            event_list = Event.objects.filter(
                approved=True,
                start_date__lte=tomorrow + datetime.timedelta(days=1),
                start_date__gte=tomorrow
            )
            if event_list:
                print('logging in. ignore 429 error.')
                ig = InstagramAPI("alfredo@1646.ca", "ag1010321")
                ig.login()  # login

                for event in event_list:
                    if event.image:
                        photo_path = event.image.path

                        caption = "Tomorrow (" + tomorrow.strftime("%m-%d-%Y") + ") in "
                        caption = caption + event.city + ":\n"
                        caption = caption + "" + event.name + "\n\n"
                        caption = caption + "learn more at sfvm.la\n\n"
                        caption = caption + "#818 #sfv #sfvm #sfvm.la"

                        ig.uploadPhoto(photo_path, caption=caption)
                    else:
                        pass

        except Exception as e:
            raise CommandError('Something went wrong')

        self.stdout.write(
            self.style.SUCCESS(
                'Tomorrow\'s events successfully posted to Instagram'
            )
        )
