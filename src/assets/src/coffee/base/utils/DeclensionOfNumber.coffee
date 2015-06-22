$ = require 'jquery'


module.exports = class DeclensionOfNumber

    @run: (number, titles) =>
        cases = [2, 0, 1, 1, 1, 2]
        key = (number % 100 > 4 && number % 100 < 20) ? 2 : cases[(number % 10 < 5) ? number % 10:5]
        console.log titles[2]
        return titles[parseInt(key)]
