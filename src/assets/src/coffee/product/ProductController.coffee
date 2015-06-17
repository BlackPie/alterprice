$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
CitySelectorView = require 'base/views/CitySelectorView'

Events = require 'product/Events'
ProductGalleryView = require 'product/views/ProductGalleryView'
ProductTabsNavigtionView = require 'product/views/tabs/ProductTabsNavigtionView'
ProductOffersLayout = require 'product/layouts/ProductOffersLayout'
#ProductTabsOffersView = require 'product/views/tabs/ProductTabsOffersView'
ProductTabsPropsView = require 'product/views/tabs/ProductTabsPropsView'
ProductTabsReviewsView = require 'product/views/tabs/ProductTabsReviewsView'
ProductOffersFilterView = require 'product/views/offers/ProductOffersFilterView'
ProductOffersListView = require 'product/views/offers/ProductOffersListView'
ProductOffersFilterState = require 'product/states/ProductOffersFilterState'
ProductOffersCollection = require 'product/collections/ProductOffersCollection'


module.exports = class ProductController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @productId = options.context.productId

        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}

        @productGalleryView = new ProductGalleryView {channel: @channel}
        @productTabsNavigtionView = new ProductTabsNavigtionView {channel: @channel}
        @productTabsPropsView = new ProductTabsPropsView {channel: @channel}
        @productTabsReviewsView = new ProductTabsReviewsView {channel: @channel}

        @productOffersLayout = new ProductOffersLayout {channel: @channel}
        @productOffersCollection = new ProductOffersCollection {id: @productId}
        @productOffersFilterView = new ProductOffersFilterView {channel: @channel}
        @productOffersListView = new ProductOffersListView {channel: @channel, collection: @productOffersCollection}
        @productOffersLayout.offersList.show(@productOffersListView)

        @productOffersCollection.fetchFiltered()

        @channel.vent.on Events.SET_OFFERS_FILTER,  @onSetOffersFilter

        @channel.vent.on Events.OPEN_OFFERS_TAB,  @openOffersTab
        @channel.vent.on Events.OPEN_PROPS_TAB,  @openPropsTab
        @channel.vent.on Events.OPEN_REVIEWS_TAB,  @openReviewsTab


    index: =>
        console.log 'index'


    openOffersTab: =>
        @productOffersLayout.show()
        @productTabsPropsView.hide()
        @productTabsReviewsView.hide()


    openPropsTab: =>
        @productTabsPropsView.show()
        @productOffersLayout.hide()
        @productTabsReviewsView.hide()


    openReviewsTab: =>
        @productTabsReviewsView.show()
        @productOffersLayout.hide()
        @productTabsPropsView.hide()


    onSetOffersFilter: =>
        filterData = @productOffersFilterView.getFilterData()
        productOffersFilterState = ProductOffersFilterState.fromArray filterData
        @productOffersCollection.fetchFiltered productOffersFilterState