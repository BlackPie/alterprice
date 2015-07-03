$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientPricelistDetailCategoriesItemView = require './ClientPricelistDetailCategoriesItemView'
PricelistCategoriesTemplate = require 'templates/client/PricelistCategories'


module.exports = class ClientPricelistDetailCategoriesCollectionView extends Marionette.CompositeView
    template: false

    childViewContainer: 'tbody'

    template: PricelistCategoriesTemplate

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ClientPricelistDetailCategoriesItemView

    childViewOptions: (model, index) =>
        return {channel: @channel}
