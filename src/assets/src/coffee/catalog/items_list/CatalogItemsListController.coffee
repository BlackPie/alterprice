$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
CitySelectorView = require 'base/views/CitySelectorView'
CatalogItemsListFilterView = require 'catalog/items_list/views/CatalogItemsListFilterView'


module.exports = class CatalogItemsListController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}
        @catalogItemsListFilterView = new CatalogItemsListFilterView {channel: @channel}


    index: () =>
        console.log 'index'