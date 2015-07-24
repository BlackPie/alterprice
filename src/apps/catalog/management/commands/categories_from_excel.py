# -*- coding: utf-8 -*-
import os
from django.core.validators import EMPTY_VALUES
from django.core.management.base import BaseCommand, CommandError
import xlrd
from catalog.models.category import Category
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        wb = xlrd.open_workbook(os.path.join(settings.BASE_DIR,
                                             'categories.xls'))
        sheet = wb.sheet_by_index(0)
        cats_db = {}
        for rnum in range(sheet.nrows):
            row = sheet.row_values(rnum)
            cats = row[0].split('/')
            path = ''
            depth = 0
            for cat in cats:
                cat_path = '/'.join((path, cat)) if path else cat
                print(path)
                if cat_path in cats_db:
                    path = cat_path
                    depth += 1
                    continue
                parent = cats_db.get(path, None)
                obj = Category(name=cat, parent=parent, depth=depth, full_path=cat_path)
                path = cat_path
                cats_db[path] = obj
                depth += 1
                obj.save()
