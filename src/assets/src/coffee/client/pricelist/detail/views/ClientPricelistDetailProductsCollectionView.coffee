$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientPricelistDetailProductsItemView = require './ClientPricelistDetailProductsItemView'
PricelistProductsTemplate = require 'templates/client/PricelistProducts'


module.exports = class ClientPricelistDetailProductsCollectionView extends Marionette.CompositeView
    childViewContainer: 'tbody'

    template: PricelistProductsTemplate

    ui:
        'countInformer': '.counter-wrapper'

    collectionEvents:
        sync: 'onSync'

    initialize: (options) =>
        @id = options.id
        @channel = options.channel

    getChildView: (model) =>
        return ClientPricelistDetailProductsItemView

    childViewOptions: (model, index) =>
        return {channel: @channel}

    onSync: (options) =>
        $.ajax
          type: 'GET'
          url: "/api/shop/yml/#{@id}/info/"
          success: (data) =>
            @$(@ui.countInformer).find('.with-card div.value').text data.product_offers
            @$(@ui.countInformer).find('.without-card div.value').text data.unassigned_offers
