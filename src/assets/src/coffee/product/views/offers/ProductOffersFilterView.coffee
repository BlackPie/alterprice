$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'product/Events'


module.exports = class ProductOffersFilterView extends Marionette.ItemView
    el: $('#product-offers-filter-view')

    template: false

    ui:
        filterLinks: '.filter-link'
        filterLinksWrapper: 'li'

    events:
        "click @ui.filterLinks": "onClickFilterLink"


    initialize: (options) =>
        @channel = options.channel


    onClickFilterLink: (e) =>
        e.preventDefault()
        newActiveLink = @$(e.target)
        newActiveLinkWrapper = newActiveLink.closest('li')
        if not newActiveLinkWrapper.hasClass 'active'
            @$(@ui.filterLinksWrapper).filter('.active').removeClass 'active'
            newActiveLinkWrapper.addClass 'active'
            deliveryType = newActiveLink.attr 'data-type'
            @channel.vent.trigger Events.SET_OFFERS_FILTER


    getFilterData: =>
        data = {}
        data['delivery_type'] = @$(@ui.filterLinksWrapper).filter('.active').find('a').attr 'data-type'
        return data