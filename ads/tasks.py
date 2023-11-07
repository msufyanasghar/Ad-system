from .models import Location

def reset_daily_visitor():
    daily_visitors = Location.objects.all()
    for daily_visitor in daily_visitors:
        daily_visitor.daily_visitors = 0
        daily_visitor.save()