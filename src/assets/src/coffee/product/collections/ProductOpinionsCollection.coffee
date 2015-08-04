PageableCollection = require "backbone.paginator"

ProductOpinionModel = require '../models/ProductOpinionModel'


module.exports = class ProductOpinionsCollection extends PageableCollection
    model: ProductOpinionModel
    url: null

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 2

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    startPageSize: 2
    showMoreSize: 1


    initialize: (options) =>
        @url = "/api/product/opinions/"


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