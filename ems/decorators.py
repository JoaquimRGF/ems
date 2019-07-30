from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse


def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('employee_list'))  # or raise PermissionDenied

        return wrap
    return decorator


# é igual ao de cima mas é só para admin
def admin_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.role == 'Admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('employee_list'))
    return wrap


def admin_hr_required(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles = ["Admin", "HR"]
        if request.role in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('employee_list'))
    return wrap
