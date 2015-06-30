$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Form = require 'base/utils/Form'


module.exports = class ClientPasswordResetFormView extends Marionette.ItemView
    el: $('#sign-in-page')

    template: false

    ui:
        form: '#client-password-reset-form-view'


    initialize: (options) =>
        @channel = options.channel
        new Form {form: @$(@ui.form)}