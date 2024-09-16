from django.http import HttpResponseForbidden
from functools import wraps


def doctor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.account.type == "Patient":
            return HttpResponseForbidden(
                "You do not have permission to view this page."
            )
        return view_func(request, *args, **kwargs)

    return _wrapped_view
