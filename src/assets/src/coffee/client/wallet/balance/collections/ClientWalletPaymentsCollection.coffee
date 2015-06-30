PageableCollection = require "backbone.paginator"

CatalogWalletPaymentModel = require '../models/CatalogWalletPaymentModel'


module.exports = class ClientWalletPaymentsCollection extends PageableCollection
    model: CatalogWalletPaymentModel
    url: "/api/client/payment/list/"

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 3

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    startPageSize: 3
    showMoreSize: 3


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