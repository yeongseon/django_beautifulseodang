import gspread
from oauth2client.service_account import ServiceAccountCredentials

from django.core.management.base import BaseCommand, CommandError
from home.models import Donation
from home.models import Book
from home.models import People

class Command(BaseCommand):

    def handle(self, *args, **options):
        Donation.objects.all().delete()
        Book.objects.all().delete()
        People.objects.all().delete()
