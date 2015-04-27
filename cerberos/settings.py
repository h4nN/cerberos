from django.conf import settings

MAX_FAILED_LOGINS = getattr(settings, 'MAX_FAILED_LOGINS', 5)

# Number of seconds after the failed access attempts are forgotten.
MEMORY_FOR_FAILED_LOGINS = getattr(settings, 'MEMORY_FOR_FAILED_LOGINS', 60*10)

USERNAME_FIELD = 'username'
