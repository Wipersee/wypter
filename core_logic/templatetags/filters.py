from django import template

register = template.Library()

def times(number):
    return range(number)

def rou(number):
    return round(number, 2)

register.filter('times', times)
register.filter('round', rou)