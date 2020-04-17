from fiCos.ext.migration import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = 'id', 'username', 'email'


user_share_schema = UserSchema()


class ItemSchema(ma.Schema):
    class Meta:
        fields = 'description', 'price'


class PromptDeliverySchema(ma.Schema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        fields = 'name', 'items'


prompt_delivery_share_schema = PromptDeliverySchema(many=True)
