from .util import get_groups

def groups_processor(request):
    print '=== request === ', request
    print '=== get_groups(request) === ', get_groups(request)
    return {'GROUPS': get_groups(request)}
