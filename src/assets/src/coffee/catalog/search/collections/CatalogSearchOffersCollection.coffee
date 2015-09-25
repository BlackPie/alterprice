PageableCollection = require "backbone.paginator"

CatalogSearchOffer = require '../models/CatalogSearchOffer'


module.exports = class CatalogSearchOffersCollection extends PageableCollection
    model: CatalogSearchOffer
    url: "/api/product/offer_search/"

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 999

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    startPageSize: 3
    showMoreSize: 3


    initialize: (options) =>
        #@channel = options.channel


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
