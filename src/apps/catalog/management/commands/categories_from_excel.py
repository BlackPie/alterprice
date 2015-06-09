# -*- coding: utf-8 -*-
from django.core.validators import EMPTY_VALUES
from django.core.management.base import BaseCommand, CommandError
from catalog.models import Category
import xlrd


class Command(BaseCommand):
    def handle(self, *args, **options):
        wb = xlrd.open_workbook('src/categories.xlsx')
        sheet = wb.sheet_by_index(0)
        rows = list()
        for rnum in range(sheet.nrows):
            rows.append(sheet.row_values(rnum))
        print(rows[0])
        categories = list()
        for r in rows:
            cats = r[0].split('/')
            cat = None
            for c in cats:
                if cat:
                    cat = Category(name=c, parent=cat)
                else:
                    cat = Category(name=c)
                    cat.save()
