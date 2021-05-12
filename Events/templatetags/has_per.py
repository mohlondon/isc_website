from django import template

register = template.Library()


def has_permission(value, arg):
    return value.has_perm(arg)


register.filter(has_permission)


def status(value):
    choices = {
        0: "Pending",
        1: "Approved",
        2: "Banned",
    }
    return choices[value]


register.filter(status)


def privilege(value,groups):
    usergroups = [group.name for group in value.groups.all()]
    for group in groups.split(','):
        if group in usergroups:
            return True
    return False

register.filter(privilege)

def checkNone(value):
    if value == None:
        return 'Not Mentioned'
    return value


register.filter(checkNone)



def GetGroups(value):
    return ",".join([group.name for group in value.groups.all()])


register.filter(GetGroups)

def SetNone(value):
    if value==None:
        return ''
    return value


register.filter(SetNone)
