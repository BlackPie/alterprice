$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Form = require 'base/utils/Form'
Select = require 'base/utils/Select'
require 'jquery-maskedinput'


module.exports = class ClientShopAddFormView extends Marionette.ItemView
    el: $('#client-shop-add-form-view')

    template: false

    ui:
        form: '#add-shop-form'
        phoneInput: '.phone-mask'
        selectWrapper: '.select'


    initialize: (options) =>
        @channel = options.channel
        new Form {form: @$(@ui.form)}
        @$(@ui.phoneInput).mask '(999) 999-9999'
        new Select @$(@ui.selectWrapper)
