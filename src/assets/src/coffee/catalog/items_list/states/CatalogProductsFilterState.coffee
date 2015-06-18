module.exports = class CatalogProductsFilterState

    constructor: (options) ->
        @price_from = options.price_from or null
        @price_till = options.price_till or null
        @brand = options.brand or null



    @createEmpty: () =>
        new CatalogProductsFilterState


    @fromArray: (data) =>
        return new ProductOffersFilterState data