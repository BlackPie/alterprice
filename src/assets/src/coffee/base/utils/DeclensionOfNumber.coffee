$ = require 'jquery'


module.exports = class DeclensionOfNumber

    @run: (number, titles) =>
        number = Math.abs number
        number %= 100
        if number >= 5 and number <= 20
            return titles[2]
        number %= 10
        if number == 1
            return titles[0]
        if number >= 2 and number <= 4
            return titles[1]
        return titles[2]
