$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Radio = require 'base/utils/Radio'
Form = require 'base/utils/Form'


module.exports = class ClientRegistrationFormView extends Marionette.ItemView
    el: $('#client-registration-form-view')

    template: false

    ui:
        form: '#registration-form'
        radioWrapper: '.radio-wrapper'


    initialize: (options) =>
        @channel = options.channel
        new Radio @$(@ui.radioWrapper)
        new Form {form: @$(@ui.form), dataType: 'html'}