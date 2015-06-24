$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class ProductOffersLayout extends Marionette.LayoutView
    el: $('#catalog-products-layout')

    regions:
        offersFilter:  "#product-offers-filter-view"
        productsList: "#catalog-products-list-view"


    #initialize: (options) =>
    #    console.log '-'


    hide: =>
        $(@el).hide()


    show: =>
        $(@el).show()