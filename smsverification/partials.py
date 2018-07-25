from tg import expose

@expose('smsverification.templates.little_partial')
def something(name):
    return dict(name=name)