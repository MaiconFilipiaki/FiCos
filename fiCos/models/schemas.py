from fiCos.ext.migration import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = 'username', 'email'


user_share_schema = UserSchema()


class ItemSchema(ma.Schema):
    class Meta:
        fields = 'id', 'description', 'price', 'length_img'


item_share_schema = ItemSchema()


class PromptDeliverySchema(ma.Schema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        fields = 'id', 'name', 'items', 'latitude', 'longitude', 'reach'


prompt_delivery_share_schema = PromptDeliverySchema()
prompt_delivery_share_schemas = PromptDeliverySchema(many=True)
