import os

from .settings import PORTAL_URL
from .urls import urlpatterns
from students.models import Group
from students.models import Student


def absoluteUrl(request):
    '''Returns absolute site root '''

    # separ = os.sep
    # domen_url_list = request.build_absolute_uri().split(separ)
    # domen_url = domen_url_list[0] + separ + separ + domen_url_list[2]

    return {'DOMEN_URL': PORTAL_URL}

def pagePathTrue(request):
    on_homepage = False
    on_journal = False
    on_groups = False
    on_exams = False
    on_contact_admin = False
    on_add = False
    page_path = request.get_full_path()

    if '/' in page_path and '/groups/' not in page_path\
        and '/journal/' not in page_path and '/exams/' not in page_path\
        and '/contact_admin' not in page_path:
        on_homepage = True
    if '/groups/' in page_path:
        on_groups = True
    if '/journal/' in page_path:
        on_journal = True
    if '/exams/' in page_path:
        on_exams = True
    if '/contact_admin' in page_path:
        on_contact_admin = True
    if '/add' in page_path:
        on_add = True

    return {'HOMEPAGE': on_homepage,
        'GROUPS': on_groups,
        'JOURNAL': on_journal,
        'EXAMS': on_exams,
        'CONTACT_ADMIN': on_contact_admin,
        'ADD': on_add}

def listStudent(request):
    return {'GROUPS_LIST': Group.objects.all()}

