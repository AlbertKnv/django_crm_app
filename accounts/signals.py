from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer

def customer_profile(sender, instance, created, **kwargs):

    if created:

        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
            )

post_save.connect(customer_profile, sender=User)


def user_profile_update(sender, instance, created, **kwargs):

    user = instance.user
    user.email=instance.email
    user.save()

post_save.connect(user_profile_update, sender=Customer)
