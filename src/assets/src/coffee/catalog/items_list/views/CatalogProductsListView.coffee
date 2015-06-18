$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
CatalogProductView = require './CatalogProductView'


module.exports = class CatalogProductsListView extends Marionette.CollectionView
    template: false

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return CatalogProductView

