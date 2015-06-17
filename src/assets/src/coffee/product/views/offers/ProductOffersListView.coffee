$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ProductOffersItemView = require './ProductOffersItemView'


module.exports = class ProductOffersListView extends Marionette.CollectionView
    template: false

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ProductOffersItemView

