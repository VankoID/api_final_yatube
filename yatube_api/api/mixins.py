from rest_framework import mixins, viewsets


class CreateListFollowModelSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    pass
