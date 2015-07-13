$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
CatalogSearchCategoryView = require './CatalogSearchCategoryView'


module.exports = class CatalogSearchCategoriesListView extends Marionette.CollectionView
    template: false

    categoriesWidth = 0

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return CatalogSearchCategoryView

    childViewOptions: (model, index) =>
        return {channel: @channel}

    #onRender: =>
    #    console.log $('#catalog-search-categories-list-view').html()
    #    @width = @width + 10
    #    console.log @collection

    #onBeforeRender: =>
    #    @width = 0


#    addChild: =>
#        console.log 'sdf'