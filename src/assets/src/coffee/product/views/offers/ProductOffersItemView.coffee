Marionette   = require 'backbone.marionette'

OfferItemTemplate = require 'templates/product/OfferItem'


module.exports = class ProductOffersItemView extends Marionette.ItemView

    serializeModel: (model) ->
        data = super(model)
        data.viewURL = model.getViewURL()
        return data

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return OfferItemTemplate(object)