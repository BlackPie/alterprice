$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

module.exports = class ProductDetailView extends Marionette.ItemView

    el: $('#item-detail-page')

    ui:
        leftBox: $('.main-info-wrapper')
        rightBox: $('.gallery-wrapper')
        descriptionWrapper: $('.description-wrapper')
        descriptionWrapperToggle: '.description-wrapper-toggle'
        opinionsTabLabel: '.tab-link[data-tab="reviews"]'

    events:
        "click @ui.descriptionWrapperToggle": "onClickToggle"

    initialize: (options) =>
        @channel = options.channel
        @fixedHeight = 200
        @descriptionToggler()
        @updateHeight()

    hideReviews: () =>
        @$(@ui.opinionsTabLabel).hide()

    updateHeight: () =>
        @unsetHeight()
        @setHeight @getMaxHeight()

    unsetHeight: () =>
        @$(@ui.leftBox).css
            minHeight: 'auto'
        @$(@ui.rightBox).css
            minHeight: 'auto'

    setHeight: (height) =>
        @$(@ui.leftBox).css
            minHeight: height
        @$(@ui.rightBox).css
            minHeight: height

    getMaxHeight: () =>
        max = 0
        if max < @$(@ui.leftBox).height() + 110 then max = @$(@ui.leftBox).height() + 110
        if max < @$(@ui.rightBox).height() + 40 then max = @$(@ui.rightBox).height() + 40
        max

    onClickToggle: (e) =>
        @$(@ui.descriptionWrapper).removeClass('bottomGradient').css
            height: @normalDescriptionHeight
        @updateHeight()

    descriptionToggler: =>
        @normalDescriptionHeight = @$(@ui.descriptionWrapper).height()
        if @normalDescriptionHeight > 300
            @$(@ui.descriptionWrapper).addClass('bottomGradient').css
                height: @fixedHeight
