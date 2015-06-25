$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Form = require 'base/utils/Form'
require 'jquery-maskedinput'


module.exports = class ClientProfileFormView extends Marionette.ItemView
    el: $('#client-profile-form-view')

    template: false

    ui:
        form: '#edit-profile-form'
        editBtn: '#profile-edit-btn'
        inputs: 'input'
        status: '.status'
        phoneInput: '.phone-mask'

    events:
        "click @ui.editBtn": "onClickEditBtn"
        "mouseenter @ui.status": "onMouseenterStatus"
        "mouseleave @ui.status": "onMouseleaveStatus"


    initialize: (options) =>
        @channel = options.channel
        new Form {form: @$(@ui.form), dataType: 'html'}
        @$(@ui.phoneInput).mask('(999) 999-9999')


    onClickEditBtn: (e) =>
        e.preventDefault()
        @$(@ui.inputs).removeAttr 'disabled'
        @$(@ui.form).addClass 'edit'


    onMouseenterStatus: (e) =>
        @$(@ui.status).find('.tooltip').fadeIn 'fast'


    onMouseleaveStatus: (e) =>
        @$(@ui.status).find('.tooltip').fadeOut 'fast'
