$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Form = require 'base/utils/Form'


module.exports = class ClientLoginFormView extends Marionette.ItemView
    el: $('#client-login-form-view')

    template: false

    ui:
        form: '#login-form'


    initialize: (options) =>
        @channel = options.channel
        new Form {form: @$(@ui.form)}