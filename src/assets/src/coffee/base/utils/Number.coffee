$ = require 'jquery'


module.exports = class Number

    constructor: (el, min) ->
        @el = $(el)
        @input = @el.find 'input[type="text"]'
        @increment = @el.find '.increment-btn'
        @decrement = @el.find '.decrement-btn'
        @value = parseInt @input.val()
        @min = min
        _ = @


        @increment.on 'click', (e) =>
            e.preventDefault()
            _.value = _.value + 1
            _.input.val _.value
            @input.change()


        @decrement.on 'click', (e) =>
            e.preventDefault()
            if _.value > @min
                _.value = _.value - 1
                _.input.val _.value
                @input.change()


        @input.on 'keypress', (e) =>
            if e.ctrlKey or e.altKey or e.metaKey
                return
            chr = Number.getChar e
            if chr == null
                return
            if chr < '0' or chr > '9'
                return false


        @input.on 'change', (e) =>
            if _.input.val() == ''
                _.value = 0
                _.input.val _.value
            else
                _.value = parseInt(_.input.val())


    @init: (elements, min = 0) =>
        elements.each (i, el) =>
            new Number el, min


    @getChar: (event) =>
        if event.which == null
            if event.keyCode < 32
                return null
            return String.fromCharCode event.keyCode
        if event.which != 0 and event.charCode != 0
            if event.which < 32
                return null
            return String.fromCharCode event.which
        return null
