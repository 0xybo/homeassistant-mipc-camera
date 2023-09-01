__all__ = ['crypto']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['b64_hmac', '_', 'a', 'str_hmac', 'hex_hmac', 'l', 'i', 'g', 'e', 'b64', 'hex', 't', 'd', 's', 'p', 'o', 'c', 'str', 'm', 'r', 'n'])
@Js
def PyJsHoisted_e_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'e', 'o'])
    var.put('o', ((Js(65535.0)&var.get('e'))+(Js(65535.0)&var.get('t'))))
    return (((((var.get('e')>>Js(16.0))+(var.get('t')>>Js(16.0)))+(var.get('o')>>Js(16.0)))<<Js(16.0))|(Js(65535.0)&var.get('o')))
PyJsHoisted_e_.func_name = 'e'
var.put('e', PyJsHoisted_e_)
@Js
def PyJsHoisted_t_(t, o, r, n, a, i, this, arguments, var=var):
    var = Scope({'t':t, 'o':o, 'r':r, 'n':n, 'a':a, 'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'o', 'a', 'r', 'n', 't'])
    return PyJsComma(var.put('t', var.get('e')(var.get('e')(var.get('o'), var.get('t')), var.get('e')(var.get('n'), var.get('i')))),var.get('e')(((var.get('t')<<var.get('a'))|PyJsBshift(var.get('t'),(Js(32.0)-var.get('a')))), var.get('r')))
PyJsHoisted_t_.func_name = 't'
var.put('t', PyJsHoisted_t_)
@Js
def PyJsHoisted_o_(e, o, r, n, a, i, l, this, arguments, var=var):
    var = Scope({'e':e, 'o':o, 'r':r, 'n':n, 'a':a, 'i':i, 'l':l, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'i', 'o', 'a', 'r', 'n', 'e'])
    return var.get('t')(((var.get('o')&var.get('r'))|((~var.get('o'))&var.get('n'))), var.get('e'), var.get('o'), var.get('a'), var.get('i'), var.get('l'))
PyJsHoisted_o_.func_name = 'o'
var.put('o', PyJsHoisted_o_)
@Js
def PyJsHoisted_r_(e, o, r, n, a, i, l, this, arguments, var=var):
    var = Scope({'e':e, 'o':o, 'r':r, 'n':n, 'a':a, 'i':i, 'l':l, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'i', 'o', 'a', 'r', 'n', 'e'])
    return var.get('t')(((var.get('o')&var.get('n'))|(var.get('r')&(~var.get('n')))), var.get('e'), var.get('o'), var.get('a'), var.get('i'), var.get('l'))
PyJsHoisted_r_.func_name = 'r'
var.put('r', PyJsHoisted_r_)
@Js
def PyJsHoisted_n_(e, o, r, n, a, i, l, this, arguments, var=var):
    var = Scope({'e':e, 'o':o, 'r':r, 'n':n, 'a':a, 'i':i, 'l':l, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'i', 'o', 'a', 'r', 'n', 'e'])
    return var.get('t')((var.get('r')^(var.get('o')|(~var.get('n')))), var.get('e'), var.get('o'), var.get('a'), var.get('i'), var.get('l'))
PyJsHoisted_n_.func_name = 'n'
var.put('n', PyJsHoisted_n_)
@Js
def PyJsHoisted_a_(a, i, this, arguments, var=var):
    var = Scope({'a':a, 'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['s', 'l', 'i', 'p', 'c', '_', 'u', 'm', 'g', 'a', 'd'])
    PyJsComma(var.get('a').put((var.get('i')>>Js(5.0)), (Js(128.0)<<(var.get('i')%Js(32.0))), '|'),var.get('a').put((Js(14.0)+(PyJsBshift((var.get('i')+Js(64.0)),Js(9.0))<<Js(4.0))), var.get('i')))
    var.put('l', Js(1732584193.0))
    var.put('s', (-Js(271733879.0)))
    var.put('c', (-Js(1732584194.0)))
    var.put('d', Js(271733878.0))
    var.put('_', Js(0.0))
    #for JS loop
    var.put('i', var.get('a').get('length'))
    while (var.get('_')<var.get('i')):
        var.put('g', var.get('l'))
        var.put('m', var.get('s'))
        var.put('p', var.get('c'))
        var.put('u', var.get('d'))
        def PyJs_LONG_0_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('l', var.get('o')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(0.0))), Js(7.0), (-Js(680876936.0)))),var.put('d', var.get('o')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(1.0))), Js(12.0), (-Js(389564586.0))))),var.put('c', var.get('o')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(2.0))), Js(17.0), Js(606105819.0)))),var.put('s', var.get('o')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))),var.put('l', var.get('o')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(4.0))), Js(7.0), (-Js(176418897.0))))),var.put('d', var.get('o')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(5.0))), Js(12.0), Js(1200080426.0)))),var.put('c', var.get('o')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))),var.put('s', var.get('o')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(7.0))), Js(22.0), (-Js(45705983.0))))),var.put('l', var.get('o')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(8.0))), Js(7.0), Js(1770035416.0)))),var.put('d', var.get('o')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))),var.put('c', var.get('o')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(10.0))), Js(17.0), (-Js(42063.0))))),var.put('s', var.get('o')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))),var.put('l', var.get('o')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(12.0))), Js(7.0), Js(1804603682.0)))),var.put('d', var.get('o')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(13.0))), Js(12.0), (-Js(40341101.0))))),var.put('c', var.get('o')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))),var.put('s', var.get('o')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(15.0))), Js(22.0), Js(1236535329.0)))),var.put('l', var.get('r')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(1.0))), Js(5.0), (-Js(165796510.0))))),var.put('d', var.get('r')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))),var.put('c', var.get('r')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(11.0))), Js(14.0), Js(643717713.0)))),var.put('s', var.get('r')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(0.0))), Js(20.0), (-Js(373897302.0))))),var.put('l', var.get('r')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(5.0))), Js(5.0), (-Js(701558691.0))))),var.put('d', var.get('r')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(10.0))), Js(9.0), Js(38016083.0)))),var.put('c', var.get('r')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(15.0))), Js(14.0), (-Js(660478335.0))))),var.put('s', var.get('r')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(4.0))), Js(20.0), (-Js(405537848.0))))),var.put('l', var.get('r')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(9.0))), Js(5.0), Js(568446438.0)))),var.put('d', var.get('r')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))),var.put('c', var.get('r')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(3.0))), Js(14.0), (-Js(187363961.0))))),var.put('s', var.get('r')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(8.0))), Js(20.0), Js(1163531501.0)))),var.put('l', var.get('r')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))),var.put('d', var.get('r')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(2.0))), Js(9.0), (-Js(51403784.0))))),var.put('c', var.get('r')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(7.0))), Js(14.0), Js(1735328473.0)))),var.put('s', var.get('r')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))),var.put('l', var.get('t')(((var.get('s')^var.get('c'))^var.get('d')), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(5.0))), Js(4.0), (-Js(378558.0))))),var.put('d', var.get('t')(((var.get('l')^var.get('s'))^var.get('c')), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))),var.put('c', var.get('t')(((var.get('d')^var.get('l'))^var.get('s')), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(11.0))), Js(16.0), Js(1839030562.0)))),var.put('s', var.get('t')(((var.get('c')^var.get('d'))^var.get('l')), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(14.0))), Js(23.0), (-Js(35309556.0))))),var.put('l', var.get('t')(((var.get('s')^var.get('c'))^var.get('d')), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))),var.put('d', var.get('t')(((var.get('l')^var.get('s'))^var.get('c')), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(4.0))), Js(11.0), Js(1272893353.0)))),var.put('c', var.get('t')(((var.get('d')^var.get('l'))^var.get('s')), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(7.0))), Js(16.0), (-Js(155497632.0))))),var.put('s', var.get('t')(((var.get('c')^var.get('d'))^var.get('l')), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))),var.put('l', var.get('t')(((var.get('s')^var.get('c'))^var.get('d')), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(13.0))), Js(4.0), Js(681279174.0)))),var.put('d', var.get('t')(((var.get('l')^var.get('s'))^var.get('c')), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(0.0))), Js(11.0), (-Js(358537222.0))))),var.put('c', var.get('t')(((var.get('d')^var.get('l'))^var.get('s')), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(3.0))), Js(16.0), (-Js(722521979.0))))),var.put('s', var.get('t')(((var.get('c')^var.get('d'))^var.get('l')), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(6.0))), Js(23.0), Js(76029189.0)))),var.put('l', var.get('t')(((var.get('s')^var.get('c'))^var.get('d')), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(9.0))), Js(4.0), (-Js(640364487.0))))),var.put('d', var.get('t')(((var.get('l')^var.get('s'))^var.get('c')), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(12.0))), Js(11.0), (-Js(421815835.0))))),var.put('c', var.get('t')(((var.get('d')^var.get('l'))^var.get('s')), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(15.0))), Js(16.0), Js(530742520.0)))),var.put('s', var.get('t')(((var.get('c')^var.get('d'))^var.get('l')), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(2.0))), Js(23.0), (-Js(995338651.0))))),var.put('l', var.get('n')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(0.0))), Js(6.0), (-Js(198630844.0))))),var.put('d', var.get('n')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(7.0))), Js(10.0), Js(1126891415.0)))),var.put('c', var.get('n')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))),var.put('s', var.get('n')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(5.0))), Js(21.0), (-Js(57434055.0))))),var.put('l', var.get('n')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(12.0))), Js(6.0), Js(1700485571.0)))),var.put('d', var.get('n')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))),var.put('c', var.get('n')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(10.0))), Js(15.0), (-Js(1051523.0))))),var.put('s', var.get('n')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))),var.put('l', var.get('n')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(8.0))), Js(6.0), Js(1873313359.0)))),var.put('d', var.get('n')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(15.0))), Js(10.0), (-Js(30611744.0))))),var.put('c', var.get('n')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))),var.put('s', var.get('n')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(13.0))), Js(21.0), Js(1309151649.0)))),var.put('l', var.get('n')(var.get('l'), var.get('s'), var.get('c'), var.get('d'), var.get('a').get((var.get('_')+Js(4.0))), Js(6.0), (-Js(145523070.0))))),var.put('d', var.get('n')(var.get('d'), var.get('l'), var.get('s'), var.get('c'), var.get('a').get((var.get('_')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))),var.put('c', var.get('n')(var.get('c'), var.get('d'), var.get('l'), var.get('s'), var.get('a').get((var.get('_')+Js(2.0))), Js(15.0), Js(718787259.0)))),var.put('s', var.get('n')(var.get('s'), var.get('c'), var.get('d'), var.get('l'), var.get('a').get((var.get('_')+Js(9.0))), Js(21.0), (-Js(343485551.0))))),var.put('l', var.get('e')(var.get('l'), var.get('g')))),var.put('s', var.get('e')(var.get('s'), var.get('m')))),var.put('c', var.get('e')(var.get('c'), var.get('p')))),var.put('d', var.get('e')(var.get('d'), var.get('u'))))
        PyJs_LONG_0_()
        # update
        var.put('_', Js(16.0), '+')
    return Js([var.get('l'), var.get('s'), var.get('c'), var.get('d')])
PyJsHoisted_a_.func_name = 'a'
var.put('a', PyJsHoisted_a_)
@Js
def PyJsHoisted_i_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 't', 'e', 'o'])
    #for JS loop
    var.put('t', Js(0.0))
    var.put('o', Js([]))
    var.put('r', ((Js(1.0)<<var.get('p'))-Js(1.0)))
    while (var.get('t')<(var.get('e').get('length')*var.get('p'))):
        var.get('o').put((var.get('t')>>Js(5.0)), ((var.get('e').callprop('charCodeAt', (var.get('t')/var.get('p')))&var.get('r'))<<(var.get('t')%Js(32.0))), '|')
        # update
        var.put('t', var.get('p'), '+')
    return var.get('o')
PyJsHoisted_i_.func_name = 'i'
var.put('i', PyJsHoisted_i_)
@Js
def PyJsHoisted_l_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'o', 'r', 'n', 't', 'e'])
    pass
    var.put('o', Js(0.0))
    var.put('r', var.get('Array')(Js(16.0)))
    var.put('n', var.get('Array')(Js(16.0)))
    var.put('l', var.get('i')(var.get('e')))
    #for JS loop
    ((Js(16.0)<var.get('l').get('length')) and var.put('l', var.get('a')(var.get('l'), (var.get('e').get('length')*var.get('p')))))
    while (Js(16.0)>var.get('o')):
        PyJsComma(var.get('r').put(var.get('o'), (Js(909522486.0)^var.get('l').get(var.get('o')))),var.get('n').put(var.get('o'), (Js(1549556828.0)^var.get('l').get(var.get('o')))))
        # update
        (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
    return PyJsComma(var.put('o', var.get('a')(var.get('r').callprop('concat', var.get('i')(var.get('t'))), (Js(512.0)+(var.get('t').get('length')*var.get('p'))))),var.get('a')(var.get('n').callprop('concat', var.get('o')), Js(640.0)))
PyJsHoisted_l_.func_name = 'l'
var.put('l', PyJsHoisted_l_)
@Js
def PyJsHoisted_s_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'e', 'o'])
    var.put('o', Js(''))
    #for JS loop
    PyJsComma(var.put('t', Js(0.0)),var.put('len', (Js(4.0)*var.get('e').get('length'))))
    while (var.get('t')<var.get('len')):
        var.put('o', (var.get('_').callprop('charAt', ((var.get('e').get((var.get('t')>>Js(2.0)))>>(((var.get('t')%Js(4.0))*Js(8.0))+Js(4.0)))&Js(15.0)))+var.get('_').callprop('charAt', ((var.get('e').get((var.get('t')>>Js(2.0)))>>((var.get('t')%Js(4.0))*Js(8.0)))&Js(15.0)))), '+')
        # update
        (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
    return var.get('o')
PyJsHoisted_s_.func_name = 's'
var.put('s', PyJsHoisted_s_)
@Js
def PyJsHoisted_c_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 't', 'e', 'o'])
    #for JS loop
    var.put('t', Js(0.0))
    var.put('o', Js(''))
    var.put('r', ((Js(1.0)<<var.get('p'))-Js(1.0)))
    while (var.get('t')<(Js(32.0)*var.get('e').get('length'))):
        var.put('o', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('e').get((var.get('t')>>Js(5.0))),(var.get('t')%Js(32.0)))&var.get('r'))), '+')
        # update
        var.put('t', var.get('p'), '+')
    return var.get('o')
PyJsHoisted_c_.func_name = 'c'
var.put('c', PyJsHoisted_c_)
@Js
def PyJsHoisted_d_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['o', 'r', 'n', 't', 'e'])
    #for JS loop
    var.put('r', Js(0.0))
    var.put('n', Js(''))
    while (var.get('r')<(Js(4.0)*var.get('e').get('length'))):
        #for JS loop
        PyJsComma(var.put('t', (((((var.get('e').get((var.get('r')>>Js(2.0)))>>((var.get('r')%Js(4.0))*Js(8.0)))&Js(255.0))<<Js(16.0))|(((var.get('e').get(((var.get('r')+Js(1.0))>>Js(2.0)))>>(((var.get('r')+Js(1.0))%Js(4.0))*Js(8.0)))&Js(255.0))<<Js(8.0)))|((var.get('e').get(((var.get('r')+Js(2.0))>>Js(2.0)))>>(((var.get('r')+Js(2.0))%Js(4.0))*Js(8.0)))&Js(255.0)))),var.put('o', Js(0.0)))
        while (Js(4.0)>var.get('o')):
            var.put('n', ((var.get('n')+var.get('m')) if (((Js(8.0)*var.get('r'))+(Js(6.0)*var.get('o')))>(Js(32.0)*var.get('e').get('length'))) else (var.get('n')+var.get('g').callprop('charAt', ((var.get('t')>>(Js(6.0)*(Js(3.0)-var.get('o'))))&Js(63.0))))))
            # update
            (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
        # update
        var.put('r', Js(3.0), '+')
    return var.get('n')
PyJsHoisted_d_.func_name = 'd'
var.put('d', PyJsHoisted_d_)
@Js
def PyJsHoisted_hex_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('s')(var.get('a')(var.get('i')(var.get('e')), (var.get('e').get('length')*var.get('p'))))
PyJsHoisted_hex_.func_name = 'hex'
var.put('hex', PyJsHoisted_hex_)
@Js
def PyJsHoisted_b64_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('d')(var.get('a')(var.get('i')(var.get('e')), (var.get('e').get('length')*var.get('p'))))
PyJsHoisted_b64_.func_name = 'b64'
var.put('b64', PyJsHoisted_b64_)
@Js
def PyJsHoisted_str_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('c')(var.get('a')(var.get('i')(var.get('e')), (var.get('e').get('length')*var.get('p'))))
PyJsHoisted_str_.func_name = 'str'
var.put('str', PyJsHoisted_str_)
@Js
def PyJsHoisted_hex_hmac_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'e'])
    return var.get('s')(var.get('l')(var.get('e'), var.get('t')))
PyJsHoisted_hex_hmac_.func_name = 'hex_hmac'
var.put('hex_hmac', PyJsHoisted_hex_hmac_)
@Js
def PyJsHoisted_b64_hmac_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'e'])
    return var.get('d')(var.get('l')(var.get('e'), var.get('t')))
PyJsHoisted_b64_hmac_.func_name = 'b64_hmac'
var.put('b64_hmac', PyJsHoisted_b64_hmac_)
@Js
def PyJsHoisted_str_hmac_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'e'])
    return var.get('c')(var.get('l')(var.get('e'), var.get('t')))
PyJsHoisted_str_hmac_.func_name = 'str_hmac'
var.put('str_hmac', PyJsHoisted_str_hmac_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.put('_', Js('0123456789abcdef'))
var.put('g', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
var.put('m', Js('='))
var.put('p', Js(8.0))
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
crypto = var.to_python()