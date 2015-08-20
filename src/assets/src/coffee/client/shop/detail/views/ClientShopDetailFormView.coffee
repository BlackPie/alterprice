$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Events = require 'client/Events'
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
        @$(@ui.phoneInput).mask('(999) 999-9999')
        new Select @$(@ui.selectWrapper)

        form = @$(@ui.form)
        inputs = @$(@ui.inputs)
        selectWrapper = @$(@ui.selectWrapper)

        new Form
            form: form
            success: =>
                inputs.attr 'disabled', 'disabled'
                form.removeClass 'edit'
                selectWrapper.addClass 'disabled'
                @channel.vent.trigger Events.SHOP_DETAIL_UPDATE_HEIGHT

    onClickEditBtn: (e) =>
        e.preventDefault()
        @$(@ui.inputs).removeAttr 'disabled'
        @$(@ui.form).addClass 'edit'
        @$(@ui.selectWrapper).removeClass 'disabled'
        @channel.vent.trigger Events.SHOP_DETAIL_UPDATE_HEIGHT


    onMouseenterStatus: (e) =>
        @$(@ui.status).find('.tooltip').fadeIn 'fast'


    onMouseleaveStatus: (e) =>
        @$(@ui.status).find('.tooltip').fadeOut 'fast'
