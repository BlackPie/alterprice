$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

CatalogSearchOffers = require 'templates/product/CatalogSearchOffers'

CatalogSearchOfferView = require './CatalogSearchOfferView'
CatalogSearchOfferEmptyView = require './CatalogSearchOfferEmptyView'


module.exports = class CatalogSearchOffersListView extends Marionette.CompositeView

    template: CatalogSearchOffers
    emptyView: CatalogSearchOfferEmptyView
    childViewContainer: '#catalog-search-offers'

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        if @collection.length == 0
            $('.items-list-page-wrapper').addClass('empty')
        else
            $('.items-list-page-wrapper').removeClass('empty')
        return CatalogSearchOfferView
