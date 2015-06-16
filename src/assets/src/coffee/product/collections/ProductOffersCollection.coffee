PageableCollection = require "backbone.paginator"

CompanyModel = require '../models/ProductOfferModel'


module.exports = class ProductOffersCollection extends PageableCollection
    model: CompanyModel
    url: "/api/company/list/"

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 10

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


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