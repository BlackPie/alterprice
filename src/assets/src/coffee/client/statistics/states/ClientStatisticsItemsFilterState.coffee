module.exports = class ClientStatisticsItemsFilterState

    constructor: (options) ->
        if options.shop
            @shop = options.shop or null
        if options.pricelist
            @pricelist = options.pricelist or null
        @period = options.period or null


    @createEmpty: () =>
        new ClientStatisticsItemsFilterState


    @fromArray: (data) =>
        return new ClientStatisticsItemsFilterState data