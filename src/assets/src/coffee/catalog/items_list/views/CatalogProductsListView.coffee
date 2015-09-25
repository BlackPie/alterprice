$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
CatalogProductView = require './CatalogProductView'
CatalogProductEmptyView = require './CatalogProductEmptyView'


module.exports = class CatalogProductsListView extends Marionette.CollectionView
    template: false

    emptyView: CatalogProductEmptyView

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        if @collection.length == 0
            $('.items-list-page-wrapper').addClass('empty')
        else
            $('.items-list-page-wrapper').removeClass('empty')
        return CatalogProductView
