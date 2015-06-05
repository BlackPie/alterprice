$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Checkbox = require 'base/utils/Checkbox'


module.exports = class CatalogItemsListFilterView extends Marionette.ItemView
    el: $('.items-filter')

    template: false

    ui:
        checkboxLabel: 'label.checkbox'
        checkboxInput: 'label.checkbox input'
        submitBtn: '.submit'

    events:
        "change @ui.checkboxInput": "onChangeCheckboxInput"


    initialize: (options) =>
        @channel = options.channel

        Checkbox.init @$(@ui.checkboxLabel)


    onChangeCheckboxInput: (e) =>
        el = @$(e.target).closest('label')
        offset = el.position()
        submitBtn = @$(@ui.submitBtn)
        console.log offset.top
        submitBtn.css 'top', offset.top
        submitBtn.fadeIn()