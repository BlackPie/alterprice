$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Form = require 'base/utils/Form'
require 'jquery-maskedinput'


module.exports = class ClientProfileEmailFormView extends Marionette.ItemView
    el: $('#client-profile-email-form-view')

    template: false

    ui:
        form: 'form'


    initialize: (options) =>
        @channel = options.channel

        form = @$(@ui.form)
        new Form
            form: form