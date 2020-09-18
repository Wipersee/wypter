from django import template

register = template.Library()

def times(number):
    return range(number)

register.filter('times', times)