$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
CitySelectorView = require 'base/views/CitySelectorView'
CatalogItemsListFilterView = require 'catalog/items_list/views/CatalogItemsListFilterView'
CatalogProductsCollection = require 'catalog/items_list/collections/CatalogProductsCollection'
CatalogProductsListView = require 'catalog/items_list/views/CatalogProductsListView'
CatalogProductsLayout = require 'catalog/items_list/layouts/CatalogProductsLayout'


module.exports = class CatalogItemsListController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel

        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}
        @catalogItemsListFilterView = new CatalogItemsListFilterView {channel: @channel}

        @catalogProductsLayout = new CatalogProductsLayout {channel: @channel}
        @catalogProductsCollection = new CatalogProductsCollection()
        @catalogProductsListView = new CatalogProductsListView {channel: @channel, collection: @catalogProductsCollection}
        @catalogProductsLayout.productsList.show(@catalogProductsListView)
        @catalogProductsCollection.fetchFiltered()


    index: () =>
        console.log 'index'
