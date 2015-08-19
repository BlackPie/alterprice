PageableCollection = require "backbone.paginator"

ClientStatisticsItemModel = require '../models/ClientStatisticsItemModel'


module.exports = class ClientStatisticsItemsCollection extends PageableCollection
    model: ClientStatisticsItemModel

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 10

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    type: 'offers'


    url: =>
        return "/api/shop/statistic/#{@type}/"
        if @pricelistId
            return "/api/shop/statistic/#{@type}/"
        else
            return "/api/shop/statistic/#{@type}/"


    stateToParams: (filterState) ->
        return filterState


    fetchFiltered: (filterState) =>
        params = @stateToParams filterState
        @filterState = filterState
        @getFirstPage({data: params, fetch: true})


    parseRecords: (response) ->
        response.results


    parseState: (response, queryParams, state, options) =>
        return {totalRecords: response.count}


    parseLinks: (resp, xhr) ->
        { next: "#{@url}" }


    setPricelistId: (id) =>
        @pricelistId = id


    setShopId: (id) =>
        @pricelistId = id

    setType: (type) =>
        @type = type
