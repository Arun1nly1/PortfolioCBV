from rest_framework import routers
from contact.views import ContactViewset

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewset)