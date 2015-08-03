ViewableModel   = require 'base/models/ViewableModel'

module.exports = class ProductOpinionModel extends ViewableModel
    idAttribute: "_nonexistent_id"

    url: null

    urlRoot: null

    getViewURL: () =>
        null
#        "/company/detail/#{@get 'slug'}/"