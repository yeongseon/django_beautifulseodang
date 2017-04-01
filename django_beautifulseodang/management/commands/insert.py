import gspread
from oauth2client.service_account import ServiceAccountCredentials

from django.core.management.base import BaseCommand, CommandError
from home.models import Donate

class Command(BaseCommand):
    help = 'insert date to donate_db'
    def handle(self, *args, **options):

        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Beautifulseodang-c0a5cc61a537.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open("donate").sheet1

        list_of_hashes = sheet.get_all_values()
        for num, name, amount in list_of_hashes:
            #print (num, name, amount)
            d = Donate(id=num, name=name, amount=amount)
            d.save()
        pass