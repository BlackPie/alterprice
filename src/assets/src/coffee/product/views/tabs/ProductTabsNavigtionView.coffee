$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Events = require 'product/Events'


module.exports = class ProductTabsNavigtionView extends Marionette.ItemView
    el: $('#product-tabs')

    template: false

    ui:
        tabLink: '.tab-link'
        tabsWrapper: '.tabs-wrapper'

    events:
        "click @ui.tabLink": "onClickTabLink"


    initialize: (options) =>
        @channel = options.channel


    onClickTabLink: (e) =>
        e.preventDefault()
        newActiveLink = @$(e.target)
        if newActiveLink.closest('a').size() > 0
            newActiveLink = newActiveLink.closest 'a'
        activeLink = @$(@ui.tabsWrapper).find '.active'
        activeLink.removeClass 'active'
        newActiveLink.closest('li').addClass 'active'

        switch newActiveLink.attr 'data-tab'
            when "offers" then @channel.vent.trigger Events.OPEN_OFFERS_TAB
            when "props" then @channel.vent.trigger Events.OPEN_PROPS_TAB
            when "reviews" then @channel.vent.trigger Events.OPEN_REVIEWS_TAB
