from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from functools import wraps


# def student(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         if not request.user.groups.filter(name="Student").exists():
#             raise PermissionDenied
#         else:
#             return func(request, *args, **kwargs)
#     return wrapper

def group_required(*group_names):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if not request.user.groups.filter(name__in=group_names).exists():
                raise PermissionDenied
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


#def is_teacher_student_or_parent(user):
    return user.groups.filter(name__in=['Teacher', 'Student', 'Parent']).exists()