$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class ProductOffersLayout extends Marionette.LayoutView
    el: $("#offers-wrapper-layout")

    regions:
        offersFilter:  ".filter-wrapper"
        offersList: ".offers-list"


    #initialize: (options) =>
    #    console.log '-'


    hide: =>
        $(@el).hide()


    show: =>
        $(@el).show()