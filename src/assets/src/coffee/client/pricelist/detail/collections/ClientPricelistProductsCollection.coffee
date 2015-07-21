PageableCollection = require "backbone.paginator"

ClientPricelistProductModel = require '../models/ClientPricelistProductModel'


module.exports = class ClientPricelistProductsCollection extends PageableCollection
    model: ClientPricelistProductModel
    #url: "/api/shop/yml/11/product/list/"

    state:
        firstPage: 1
        currentPage: 1
        pageSize: 20

    queryParams:
        currentPage: "page"
        pageSize: "page_size"


    url: =>
        return "/api/shop/yml/#{@pricelistId}/product/list/"


    stateToParams: (filterState) ->
        return filterState


    fetchFiltered: (filterState) =>
        params = @stateToParams filterState
        @filterState = filterState
        @getFirstPage({data: params, fetch: true})


    parseRecords: (response) ->
        results = []
        prevCategory = false
        for result in response.results
            if result.category != prevCategory
                results.push
                    category: result.category
                    is_category: true

            results.push
                product_url: result.product_url
                product: result.product
                click_price: result.click_price
                category: result.category
                is_category: false

            prevCategory = result.category

        results


    parseState: (response, queryParams, state, options) =>
        return {totalRecords: response.count}


    parseLinks: (resp, xhr) ->
        { next: "#{@url}" }


    setPricelistId: (id) =>
        @pricelistId = id