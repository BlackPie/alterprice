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

        #@sync()

        @currentValue.on 'click', (e) =>
            e.preventDefault()
            _.open()

        @overlay.on 'click', (e) =>
            e.preventDefault()
            _.close()

        @choices.click (e) =>
            console.log 'asdf'
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
