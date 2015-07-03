Marionette   = require 'backbone.marionette'

PricelistProductItemTemplate = require 'templates/client/PricelistProductItem'


module.exports = class ClientPricelistDetailProductsItemView extends Marionette.ItemView
    tagName: 'tr'

    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return PricelistProductItemTemplate(object)