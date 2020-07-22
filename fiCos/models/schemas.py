from fiCos.ext.migration import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = 'username', 'email'


user_share_schema = UserSchema()


class ImgItemSchema(ma.Schema):
    class Meta:
        fields = 'id', 'nameImg'

img_item_share_schema = ImgItemSchema()

class ItemSchema(ma.Schema):
    imgs = ma.Nested(ImgItemSchema, many=True)
    class Meta:
        fields = 'id', 'description', 'price', 'length_img', 'imgs'


item_share_schema = ItemSchema()
item_share_schemas = ItemSchema(many=True)


class PromptDeliverySchema(ma.Schema):
    items = ma.Nested(ItemSchema, many=True)
    latitude = ma.Decimal()
    longitude = ma.Decimal()
    class Meta:
        fields = 'id', 'name', 'items', 'latitude', 'longitude', 'reach'


prompt_delivery_share_schema = PromptDeliverySchema()
prompt_delivery_share_schemas = PromptDeliverySchema(many=True)
