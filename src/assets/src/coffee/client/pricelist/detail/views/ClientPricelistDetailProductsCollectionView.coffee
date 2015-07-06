$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientPricelistDetailProductsItemView = require './ClientPricelistDetailProductsItemView'
PricelistProductsTemplate = require 'templates/client/PricelistProducts'


module.exports = class ClientPricelistDetailProductsCollectionView extends Marionette.CompositeView
    template: false

    childViewContainer: 'tbody'

    template: PricelistProductsTemplate

    ui:
        'countInformer': '.all-counter'

    collectionEvents:
        sync: 'onSync'

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ClientPricelistDetailProductsItemView

    childViewOptions: (model, index) =>
        return {channel: @channel}

    onSync: (options) =>
        console.log 'asd1'
        console.log options
        @$(@ui.countInformer).find('div.value').text options.state.totalRecords