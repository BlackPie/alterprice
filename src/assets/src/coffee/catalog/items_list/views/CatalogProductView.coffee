Marionette   = require 'backbone.marionette'

ProductCardTemplate = require 'templates/product/ProductCard'


module.exports = class CatalogProductView extends Marionette.ItemView
    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return ProductCardTemplate(object)
