ViewableModel   = require 'base/models/ViewableModel'

module.exports = class ProductOfferModel extends ViewableModel
    idAttribute: "_nonexistent_id"

    url: "/api/company/"

    urlRoot: "/api/company/"

    getViewURL: () =>
        "/company/detail/#{@get 'slug'}/"