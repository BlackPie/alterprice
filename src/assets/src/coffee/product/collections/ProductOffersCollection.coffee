PageableCollection = require "backbone.paginator"

ProductOfferModel = require '../models/ProductOfferModel'


module.exports = class ProductOffersCollection extends PageableCollection
    model: ProductOfferModel
    url: null

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 3

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    startPageSize: 3
    showMoreSize: 10


    initialize: (options) =>
        @url = "/api/product/detail/#{options.id}/offers/"


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