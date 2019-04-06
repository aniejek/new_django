import random

with open("new_django/secret", "w") as secret:
    secret.write(''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)))
