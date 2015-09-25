Marionette   = require 'backbone.marionette'

CatalogOfferTemplate = require 'templates/product/CatalogOffer'

module.exports = class CatalogSearchOfferView extends Marionette.ItemView

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return CatalogOfferTemplate(object)
