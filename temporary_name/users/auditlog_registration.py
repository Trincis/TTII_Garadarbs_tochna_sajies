from auditlog.registry import auditlog
from .models import User

auditlog.register(User)