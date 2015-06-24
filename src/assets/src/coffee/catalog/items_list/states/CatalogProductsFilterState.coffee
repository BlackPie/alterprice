module.exports = class CatalogProductsFilterState

    constructor: (options) ->
        @price_min = options.price_min or null
        @price_max = options.price_max or null
        @brand = options.brand or null
        @category = options.category or null
        @search = options.search or null



    @createEmpty: () =>
        new CatalogProductsFilterState


    @fromArray: (data) =>
        return new CatalogProductsFilterState data