$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'client/Events'

Form = require 'base/utils/Form'


module.exports = class ClientPriceListDetailParamsFormView extends Marionette.ItemView
    el: $('#client-pricelist-detail-params-form-vew')

    template: false

    ui:
        form: '#client-pricelist-detail-form'
        editBtn: '#pricelist-edit-btn'
        inputs: 'input'

    events:
        "click @ui.editBtn": "onClickEditBtn"


    initialize: (options) =>
        @channel = options.channel
        form = @$(@ui.form)
        inputs = @$(@ui.inputs)
        new Form
            form: form
            success: =>
                inputs.attr 'disabled', 'disabled'
                form.removeClass 'edit'
                @channel.vent.trigger Events.PRICELIST_CHANGE_TITLE, form.find('input[name="name"]').val()


    onClickEditBtn: (e) =>
        e.preventDefault()
        @$(@ui.inputs).removeAttr 'disabled'
        @$(@ui.form).addClass 'edit'
