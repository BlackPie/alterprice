$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Form = require 'base/utils/Form'
require 'jquery-maskedinput'


module.exports = class ClientProfilePasswordFormView extends Marionette.ItemView
    el: $('#client-profile-password-form-view')

    template: false

    ui:
        form: '#client-profile-password-form'


    initialize: (options) =>
        @channel = options.channel

        form = @$(@ui.form)
        new Form
            form: form