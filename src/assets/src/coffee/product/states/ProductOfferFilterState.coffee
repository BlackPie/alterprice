module.exports = class ProductOfferFilterState

    constructor: (search = null, category = null, subcategory = null) ->
        @search = search
        @category = category
        @subcategory = subcategory


    @createEmpty: () =>
        new CompanySearchState


    @fromArray: (data) =>
        return new CompanySearchState(
            data.search or null,
            data.category or null,
            data.subcategory or null
        )