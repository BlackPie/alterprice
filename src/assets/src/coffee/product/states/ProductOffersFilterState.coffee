module.exports = class ProductOffersFilterState

    constructor: (deliveryType = null) ->
        @delivery_type = deliveryType


    @createEmpty: () =>
        new ProductOffersFilterState


    @fromArray: (data) =>
        return new ProductOffersFilterState data.delivery_type