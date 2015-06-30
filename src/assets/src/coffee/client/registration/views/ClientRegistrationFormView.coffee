$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Radio = require 'base/utils/Radio'
Form = require 'base/utils/Form'
Checkbox = require 'base/utils/Checkbox'
require 'jquery-maskedinput'


module.exports = class ClientRegistrationFormView extends Marionette.ItemView
    el: $('#client-registration-form-view')

    template: false

    ui:
        form: '#registration-form'
        radioWrapper: '.radio-wrapper'
        phoneInput: '.phone-mask'
        selectWrapper: '.select'
        checkboxWrapper: 'label.checkbox'
        showOperatorCodeBtn: '.operator-code-show-link'

    events:
        "click @ui.showOperatorCodeBtn": "onClickShowOperatorCodeBtn"


    initialize: (options) =>
        @channel = options.channel
        new Radio @$(@ui.radioWrapper)
        new Form {form: @$(@ui.form)}
        @$(@ui.phoneInput).mask('(999) 999-9999')
        Checkbox.init @$(@ui.checkboxWrapper)


    onClickShowOperatorCodeBtn: (e) =>
        e.preventDefault()
        @$(e.target).closest('.field-wrapper').find('.field-value').slideToggle 'fast'
