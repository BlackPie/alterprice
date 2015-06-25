$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Form = require 'base/utils/Form'
Select = require 'base/utils/Select'
require 'jquery-maskedinput'


module.exports = class ClientShopDetailFormView extends Marionette.ItemView
    el: $('#client-shop-detail-form-view')

    template: false

    ui:
        form: '#edit-profile-form'
        editBtn: '#shop-edit-btn'
        inputs: 'input'
        status: '.status'
        phoneInput: '.phone-mask'
        selectWrapper: '.select'

    events:
        "click @ui.editBtn": "onClickEditBtn"
        "mouseenter @ui.status": "onMouseenterStatus"
        "mouseleave @ui.status": "onMouseleaveStatus"


    initialize: (options) =>
        @channel = options.channel
        new Form {form: @$(@ui.form), dataType: 'html'}
        @$(@ui.phoneInput).mask('(999) 999-9999')
        new Select @$(@ui.selectWrapper)


    onClickEditBtn: (e) =>
        e.preventDefault()
        @$(@ui.inputs).removeAttr 'disabled'
        @$(@ui.form).addClass 'edit'
        @$(@ui.selectWrapper).removeClass 'disabled'


    onMouseenterStatus: (e) =>
        @$(@ui.status).find('.tooltip').fadeIn 'fast'


    onMouseleaveStatus: (e) =>
        @$(@ui.status).find('.tooltip').fadeOut 'fast'
