$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
CatalogSearchCategoryView = require './CatalogSearchCategoryView'


module.exports = class CatalogSearchCategoriesListView extends Marionette.CollectionView
    template: false

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return CatalogSearchCategoryView

    childViewOptions: (model, index) =>
        return {channel: @channel}