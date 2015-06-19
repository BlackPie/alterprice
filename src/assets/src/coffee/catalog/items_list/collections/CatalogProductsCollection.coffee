PageableCollection = require "backbone.paginator"

CatalogProductModel = require '../models/CatalogProductModel'


module.exports = class CatalogProductsCollection extends PageableCollection
    model: CatalogProductModel
    url: "/api/product/list/"

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 2

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    startPageSize: 2
    showMoreSize: 1


    #initialize: (options) =>



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