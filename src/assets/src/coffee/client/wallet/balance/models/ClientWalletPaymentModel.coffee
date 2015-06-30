ViewableModel   = require 'base/models/ViewableModel'

module.exports = class ClientWalletPaymentModel extends ViewableModel
    idAttribute: "_nonexistent_id"

    url: null

    urlRoot: null

    getViewURL: () =>
        null