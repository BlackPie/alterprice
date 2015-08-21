PageableCollection = require "backbone.paginator"

CatalogSearchCategoryLink = require '../models/CatalogSearchCategoryLink'


module.exports = class CatalogSearchCategoryLinksCollection extends PageableCollection
    model: CatalogSearchCategoryLink
    url: "/api/product/search/"

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 999

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    startPageSize: 3
    showMoreSize: 3


    #initialize: (options) =>



    stateToParams: (filterState) ->
        return filterState


    fetchFiltered: (filterState) =>
        params = @stateToParams filterState
        @filterState = filterState
        @getFirstPage({data: params, fetch: true})


    parseRecords: (response) ->
        response.categories


    parseState: (response, queryParams, state, options) =>
        return {totalRecords: response.count}


    parseLinks: (resp, xhr) ->
        { next: "#{@url}" }
