import gspread
from oauth2client.service_account import ServiceAccountCredentials

from django.core.management.base import BaseCommand, CommandError
from home.models import Content

class Command(BaseCommand):
    help = 'insert date to donate_db'
    def handle(self, *args, **options):

        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Beautifulseodang-c0a5cc61a537.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open("content").sheet1

        Content.objects.all().delete()
        i = 0
        for _type, _number, _name, _author, _img in sheet.get_all_values():
            if i == 0:
                pass
            else:
                print(_type, _number, _name, _author, _img)
                content = Content(type=_type, number=_number, name=_name, author=_author, img=_img)
                content.save()
            i += 1