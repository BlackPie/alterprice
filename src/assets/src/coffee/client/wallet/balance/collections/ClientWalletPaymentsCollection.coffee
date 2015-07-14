PageableCollection = require "backbone.paginator"

ClientWalletPaymentModel = require '../models/ClientWalletPaymentModel'


module.exports = class ClientWalletPaymentsCollection extends PageableCollection
    model: ClientWalletPaymentModel
    url: "/api/user/payment/list/"

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