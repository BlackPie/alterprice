Number = require 'base/utils/Number'

template = (locals) =>
    if locals.payment_type == 0
        paymentType = 'банковский счет'
    else
        paymentType = 'онлайн оплата'

    return "
        <td>#{locals.amount}</td>
        <td>#{locals.created}</td>
        <td>#{paymentType}</td>
    "


module.exports = template