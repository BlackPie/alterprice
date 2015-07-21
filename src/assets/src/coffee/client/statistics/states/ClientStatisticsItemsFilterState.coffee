module.exports = class ClientStatisticsItemsFilterState

    constructor: (options) ->
        @shop = options.shop or null
        @period = options.period or null


    @createEmpty: () =>
        new ClientStatisticsItemsFilterState


    @fromArray: (data) =>
        return new ClientStatisticsItemsFilterState data