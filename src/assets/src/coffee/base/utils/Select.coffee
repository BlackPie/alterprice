$ = require 'jquery'


module.exports = class Select

    constructor: (el) ->
        @el = $(el)
        @select = @el.find('select')
        @wrapper = @el.find('.select-wrapper')
        @currentValue = @wrapper.find('.current-value')
        @overlay = @el.find('.overlay')
        @choices = @wrapper.find('.choice')
        _ = @

        @currentValue.on 'click', (e) =>
            e.preventDefault()
            if not _.el.hasClass 'disabled'
                _.open()

        @overlay.on 'click', (e) =>
            e.preventDefault()
            _.close()

        @choices.click (e) =>
            e.preventDefault()
            el = $(e.target)
            value = el.attr('data-value')
            text = el.text()
            _.select.val(value)
            _.currentValue.text(text)
            _.close()


    open: =>
        @el.addClass('opened')


    close: =>
        @el.removeClass('opened')
