import gspread
from oauth2client.service_account import ServiceAccountCredentials

from django.core.management.base import BaseCommand, CommandError
from home.models import People

class Command(BaseCommand):
    help = 'insert date to donate_db'
    def handle(self, *args, **options):

        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Beautifulseodang-c0a5cc61a537.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open("people").sheet1

        i = 0
        for _type, _name, _carrier, _region, _img in sheet.get_all_values():
            if i == 0 :
                pass
            print(_type, _name, _carrier, _region, _img)
            people = People(type = _type, name = _name, carrier = _carrier, region = _region, image = _img)
            people.save()
            i += 1