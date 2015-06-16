$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
CitySelectorView = require 'base/views/CitySelectorView'

Events = require 'product/Events'
ProductGalleryView = require 'product/views/ProductGalleryView'
ProductTabsNavigtionView = require 'product/views/tabs/ProductTabsNavigtionView'
ProductTabsOffersView = require 'product/views/tabs/ProductTabsOffersView'
ProductTabsPropsView = require 'product/views/tabs/ProductTabsPropsView'
ProductTabsReviewsView = require 'product/views/tabs/ProductTabsReviewsView'


module.exports = class ProductController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}

        @productGalleryView = new ProductGalleryView {channel: @channel}
        @productTabsNavigtionView = new ProductTabsNavigtionView {channel: @channel}
        @productTabsOffersView = new ProductTabsOffersView {channel: @channel}
        @productTabsPropsView = new ProductTabsPropsView {channel: @channel}
        @productTabsReviewsView = new ProductTabsReviewsView {channel: @channel}

        @channel.vent.on Events.OPEN_OFFERS_TAB,  @openOffersTab
        @channel.vent.on Events.OPEN_PROPS_TAB,  @openPropsTab
        @channel.vent.on Events.OPEN_REVIEWS_TAB,  @openReviewsTab


    index: =>
        console.log 'index'


    openOffersTab: =>
        @productTabsOffersView.show()
        @productTabsPropsView.hide()
        @productTabsReviewsView.hide()
        console.log '1'


    openPropsTab: =>
        @productTabsPropsView.show()
        @productTabsOffersView.hide()
        @productTabsReviewsView.hide()
        console.log '2'


    openReviewsTab: =>
        @productTabsReviewsView.show()
        @productTabsOffersView.hide()
        @productTabsPropsView.hide()
        console.log '3'