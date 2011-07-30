from tastypie.resources import ModelResource
from tastypie.fields import ToOneField
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from mb.models import Artist, ArtistName
# Generally this is not happymaking

class ArtistResource(ModelResource):
    name = ToOneField("mb.api.ArtistNameResource", "name", full=True)
    
    class Meta:
        queryset = Artist.objects.all()
        allowed_methods = ["get", "put", "post", "delete"]
        authorization = Authorization()
        authentication = Authentication()


class ArtistNameResource(ModelResource):
    
    class Meta:
        queryset = ArtistName.objects.all()
        allowed_methods = ["get", "put", "post", "delete"]
        authorization = Authorization()
        authentication = Authentication()
