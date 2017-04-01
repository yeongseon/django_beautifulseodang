import gspread
from oauth2client.service_account import ServiceAccountCredentials

from django.core.management.base import BaseCommand, CommandError
from home.models import EastBook

class Command(BaseCommand):
    help = 'insert date to donate_db'
    def handle(self, *args, **options):

        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Beautifulseodang-c0a5cc61a537.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open("book").sheet1

        for _num, _name, _author, _img in sheet.get_all_values():
            print (_num, _name, _author, _img)
            eastbook = EastBook(id=_num, name=_name, author=_author, img=_img)
            eastbook.save()
        pass