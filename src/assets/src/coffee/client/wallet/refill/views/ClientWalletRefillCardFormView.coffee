$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Radio = require 'base/utils/Radio'
Form = require 'base/utils/Form'


module.exports = class ClientWalletRefillCardFormView extends Marionette.ItemView
    el: $('#client-wallet-refill-card-form-view')

    template: false

    ui:
        form: '#client-wallet-refill-card-form'
        tabContainer: '.tab-content'


    initialize: (options) =>
        @channel = options.channel
        new Radio @$(@ui.radioWrapper)
        new Form {form: @$(@ui.form)}


    closeTab: =>
        @$(@ui.tabContainer).slideUp 'fast'


    openTab: =>
        @$(@ui.tabContainer).slideDown 'fast'

