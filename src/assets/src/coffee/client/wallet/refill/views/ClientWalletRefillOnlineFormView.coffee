$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Radio = require 'base/utils/Radio'
Form = require 'base/utils/Form'
Number = require 'base/utils/Number'


module.exports = class ClientWalletRefillOnlineFormView extends Marionette.ItemView
    el: $('#client-wallet-refill-online-form-view')

    template: false

    ui:
        form: '#client-wallet-refill-online-form'
        radioWrapper: '.radio-wrapper'
        tabContainer: '.tab-content'
        quantumInput: '#quantum-input'

    events:
        "keypress @ui.quantumInput": "onKeypressQuantumInput"


    initialize: (options) =>
        @channel = options.channel
        new Radio @$(@ui.radioWrapper)
        new Form {form: @$(@ui.form)}


    onKeypressQuantumInput: (e) =>
        if e.ctrlKey or e.altKey or e.metaKey
            return
        chr = Number.getChar e
        if chr == null
            return
        if chr < '0' or chr > '9'
            return false


    closeTab: =>
        @$(@ui.tabContainer).slideUp 'fast'


    openTab: =>
        @$(@ui.tabContainer).slideDown 'fast'
