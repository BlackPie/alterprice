PageableCollection = require "backbone.paginator"

ClientStatisticsItemModel = require '../models/ClientStatisticsItemModel'


module.exports = class ClientStatisticsItemsCollection extends PageableCollection
    model: ClientStatisticsItemModel

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 999

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    url: =>
        return "/api/shop/statistic/shop/"


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