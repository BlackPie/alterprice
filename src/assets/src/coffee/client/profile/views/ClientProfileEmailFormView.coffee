$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'client/Events'

Form = require 'base/utils/Form'
require 'jquery-maskedinput'


module.exports = class ClientProfileEmailFormView extends Marionette.ItemView
    el: $('#client-profile-email-form-view')

    template: false

    ui:
        form: 'form'
        newEmail: '.new-email'

    events:
        "keyup @ui.newEmail": "onChangeNewEmail"


    initialize: (options) =>
        @channel = options.channel

        form = @$(@ui.form)
        new Form
            form: form
            success: =>
                @channel.vent.trigger Events.PROFILE_CHANGE_EMAIL, @newEmail


    onChangeNewEmail: (e) =>
        @newEmail =  @$(@ui.newEmail).val()