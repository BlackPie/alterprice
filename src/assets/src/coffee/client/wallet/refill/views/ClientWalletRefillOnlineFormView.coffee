$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Radio = require 'base/utils/Radio'
Form = require 'base/utils/Form'


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
        chr = @getChar e
        if chr == null
            return
        if chr < '0' or chr > '9'
            return false


    closeTab: =>
        @$(@ui.tabContainer).slideUp 'fast'


    openTab: =>
        @$(@ui.tabContainer).slideDown 'fast'


    getChar: (event) =>
        if event.which == null
            if event.keyCode < 32
                return null
            return String.fromCharCode event.keyCode
        if event.which != 0 and event.charCode != 0
            if event.which < 32
                return null
            return String.fromCharCode event.which
        return null

