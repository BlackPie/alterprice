PageableCollection = require "backbone.paginator"

ClientPricelistCategoryModel = require '../models/ClientPricelistCategoryModel'


module.exports = class ClientPricelistCategoriesCollection extends PageableCollection
    model: ClientPricelistCategoryModel

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 999

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    url: =>
        return "/api/shop/yml/#{@pricelistId}/category/list/"


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