from import_export import resources
from core.models import *

class StudentInformationResource(resources.ModelResource):
    class Meta:
        model = StudentInformation