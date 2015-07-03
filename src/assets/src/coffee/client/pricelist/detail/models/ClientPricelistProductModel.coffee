ViewableModel   = require 'base/models/ViewableModel'

module.exports = class ClientPricelistProductModel extends ViewableModel
    idAttribute: "_nonexistent_id"

    url: null

    urlRoot: null

    getViewURL: () =>
        null