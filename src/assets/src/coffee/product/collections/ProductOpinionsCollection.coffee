PageableCollection = require "backbone.paginator"
Events = require 'product/Events'
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
        @channel = options.channel


    stateToParams: (filterState) ->
        return filterState


    fetchFiltered: (filterState) =>
        params = @stateToParams filterState
        @filterState = filterState
        @getFirstPage({data: params, fetch: true})


    parseRecords: (response) ->
        response.results


    parseState: (response, queryParams, state, options) =>
        if response.count < 1
            @channel.vent.trigger Events.OPINIONS_NULL
        return {totalRecords: response.count}


    parseLinks: (resp, xhr) ->
        { next: "#{@url}" }
