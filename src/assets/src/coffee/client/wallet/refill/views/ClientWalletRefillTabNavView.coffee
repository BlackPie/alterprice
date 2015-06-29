$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'client/Events'


module.exports = class ClientWalletRefillTabNavView extends Marionette.ItemView
    el: $('#client-wallet-refill-view')

    template: false

    ui:
        tabNavWrapper: '.tabs-nav'
        tabNavLink: '.tab-link'
        tabNavLinkWrapper: 'li'

    events:
        "click @ui.tabNavLink": "onClickTabNavLink"


    initialize: (options) =>
        @channel = options.channel


    onClickTabNavLink: (e) =>
        e.preventDefault()
        target = $(e.target)
        wrapper = target.closest('li')
        if not wrapper.hasClass 'active'
            tabName = target.attr 'data-tab'
            @$(@ui.tabNavWrapper).find('.active').removeClass 'active'
            wrapper.addClass('active')
            @channel.vent.trigger Events.WALLET_REFILL_CHANGE_TAB, tabName

