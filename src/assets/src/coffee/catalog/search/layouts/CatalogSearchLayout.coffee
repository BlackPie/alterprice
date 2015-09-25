$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class CatalogSearchLayout extends Marionette.LayoutView
    el: $('#catalog-products-layout')

    regions:
        offersFilter:  "#product-offers-filter-view"
        productsList: "#catalog-products-list-view"
        categoriesList: "#catalog-search-categories-list-view-wrapper"
        offersList: "#catalog-offers-layout"

    hide: =>
        $(@el).hide()


    show: =>
        $(@el).show()
