__all__ = ['mcodec']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['f', 'C', 'l', 'u', 'g', 'b', 'B', 'e', 'K', 'A', 'mcodec', 't', 'd', 's', 'q', 'c', 'v', 'h', 'm', 'F', 'r'])
@Js
def PyJsHoisted_f_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a'])
    return (((var.get('a') if var.get('a') else Js('%'))+var.get('v').callprop('charAt', (var.get('c')>>Js(4.0))))+var.get('v').callprop('charAt', (var.get('c')&Js(15.0))))
PyJsHoisted_f_.func_name = 'f'
var.put('f', PyJsHoisted_f_)
@Js
def PyJsHoisted_e_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return ((var.get('a')-Js(48.0)) if ((Js(48.0)<=var.get('a')) and (Js(57.0)>=var.get('a'))) else ((var.get('a')-Js(55.0)) if ((Js(65.0)<=var.get('a')) and (Js(71.0)>=var.get('a'))) else ((var.get('a')-Js(87.0)) if ((Js(97.0)<=var.get('a')) and (Js(102.0)>=var.get('a'))) else Js(0.0))))
PyJsHoisted_e_.func_name = 'e'
var.put('e', PyJsHoisted_e_)
@Js
def PyJsHoisted_d_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'f', 'c', 'g', 'a', 'b', 'd'])
    var.put('f', Js(''))
    var.put('l', (Js('')+var.get('a')))
    if (Js(0.0)==var.get('l').callprop('indexOf', Js('0x'))):
        #for JS loop
        var.put('b', (var.get('l').get('length')-Js(1.0)))
        while (Js(1.0)<var.get('b')):
            #for JS loop
            var.put('d', var.put('g', Js(0.0)))
            while ((Js(8.0)>var.get('d')) and (Js(1.0)<var.get('b'))):
                var.put('g', (var.get('e')(var.get('l').callprop('charCodeAt', var.get('b')))<<var.get('d')), '+')
                # update
                PyJsComma(var.put('b',Js(var.get('b').to_number())-Js(1)),var.put('d', Js(4.0), '+'))
            var.put('f', (var.get('s')(var.get('g'))+var.get('f')))

    else:
        #for JS loop
        var.put('b', Js(24.0))
        while (Js(0.0)<=var.get('b')):
            ((var.get('a')>=(Js(1.0)<<var.get('b'))) and var.put('f', var.get('s')(((var.get('a')>>var.get('b'))&Js(255.0))), '+'))
            # update
            var.put('b', Js(8.0), '-')
    #for JS loop

    while (var.get('f').get('length')<var.get('c')):
        var.put('f', (Js('\x00')+var.get('f')))

    return var.get('f')
PyJsHoisted_d_.func_name = 'd'
var.put('d', PyJsHoisted_d_)
@Js
def PyJsHoisted_b_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'f', 'c', 'h', 'm', 'g', 'a', 'b', 'e', 'd'])
    #for JS loop
    var.put('f', Js(0.0))
    var.put('l', Js(''))
    var.put('h', var.get('a').get('length'))
    var.put('m', (var.get('A') if var.get('c') else var.get('u')))
    while (var.get('f')<var.get('h')):
        #for JS loop
        var.put('d', Js(0.0))
        while ((Js(24.0)>var.get('d')) and (var.get('f')<var.get('h'))):
            var.put('b', ((var.get('b')<<Js(8.0))+var.get('a').callprop('charCodeAt', var.get('f'))))
            # update
            PyJsComma(var.put('d', Js(8.0), '+'),var.put('f',Js(var.get('f').to_number())+Js(1)))
        #for JS loop
        var.put('g', Js(0.0))
        while (Js(24.0)>var.get('g')):
            PyJsComma(var.put('e', ((var.get('d')-var.get('g'))-Js(6.0))),var.put('l', (var.get('m').callprop('charAt', ((var.get('b')<<(-var.get('e'))) if (Js(0.0)>var.get('e')) else (var.get('b')>>var.get('e')))) if (var.get('g')<var.get('d')) else Js('')), '+'))
            # update
            PyJsComma(var.put('g', Js(6.0), '+'),var.put('b', ((Js(1.0)<<(var.get('d')-var.get('g')))-Js(1.0)), '&'))

    return var.get('l')
PyJsHoisted_b_.func_name = 'b'
var.put('b', PyJsHoisted_b_)
@Js
def PyJsHoisted_g_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'a', 'c', 'h', 'm', 'g', 'r', 'b', 'e', 'd'])
    var.put('r', Js(''))
    var.put('e', Js(0.0))
    #for JS loop
    var.put('h', var.get('a').get('length'))
    while (var.get('e')<var.get('h')):
        if (Js(127.0)>=var.put('d', var.get('a').callprop('charCodeAt', var.get('e')))):
            var.put('r', (var.get('f')(var.get('c'), var.get('d')) if var.get('C').get(var.put('b', var.get('a').callprop('charAt', var.get('e')))) else var.get('b')), '+')
        else:
            var.put('m', Js(''))
            #for JS loop
            var.put('g', var.put('l', (Js(0.0) if (Js(128.0)>var.get('d')) else (Js(1.0) if (Js(2048.0)>var.get('d')) else (Js(2.0) if (Js(65536.0)>var.get('d')) else (Js(3.0) if (Js(4194304.0)>var.get('d')) else (Js(4.0) if (Js(134217728.0)>var.get('d')) else Js(5.0))))))))
            while (Js(0.0)<var.get('g')):
                var.put('m', (var.get('f')(var.get('c'), (Js(128.0)|(var.get('d')&Js(63.0))))+var.get('m')))
                # update
                PyJsComma(var.put('g',Js(var.get('g').to_number())-Js(1)),var.put('d', Js(6.0), '>>'))
            var.put('d', var.get('t').get(var.get('l')), '|')
            var.put('r', (var.get('f')(var.get('c'), var.get('d'))+var.get('m')), '+')
        # update
        var.put('e',Js(var.get('e').to_number())+Js(1))
    return var.get('r')
PyJsHoisted_g_.func_name = 'g'
var.put('g', PyJsHoisted_g_)
@Js
def PyJsHoisted_h_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'f', 'a', 'c', 'h', 'm', 'g', 'r', 'b', 'd'])
    var.put('f', var.get('a').get('length'))
    var.put('r', Js(''))
    var.put('c', (var.get('c') or Js('%')))
    #for JS loop
    var.put('g', Js(0.0))
    while (var.get('g')<var.get('f')):
        if ((var.get('c')!=var.get('a').callprop('charAt', var.get('g'))) or ((var.get('g')+Js(3.0))>var.get('f'))):
            PyJsComma(var.put('r', var.get('a').callprop('charAt', var.get('g')), '+'),var.put('g',Js(var.get('g').to_number())+Js(1)))
        else:
            var.put('b', ((var.get('e')((var.get('a').callprop('charCodeAt', (var.get('g')+Js(1.0)))&Js(255.0)))<<Js(4.0))+var.get('e')((var.get('a').callprop('charCodeAt', (var.get('g')+Js(2.0)))&Js(255.0)))))
            var.put('l', var.get('t').get('length'))
            #for JS loop
            var.put('d', Js(0.0))
            while (Js(1.0)<var.get('l')):
                if (var.get('b')>=var.get('t').get((var.get('l')-Js(1.0)))):
                    if (var.put('m', (var.get('g')+(Js(3.0)*var.get('l'))))<=var.get('f')):
                        var.put('d', (var.get('b')-var.get('t').get((var.get('l')-Js(1.0)))))
                        #for JS loop
                        var.put('h', (var.get('g')+Js(3.0)))
                        while ((var.get('h')<var.get('m')) and (var.get('c')==var.get('a').callprop('charAt', var.get('h')))):
                            var.put('d', ((var.get('d')<<Js(6.0))+(((var.get('e')((var.get('a').callprop('charCodeAt', (var.get('h')+Js(1.0)))&Js(255.0)))<<Js(4.0))+var.get('e')((var.get('a').callprop('charCodeAt', (var.get('h')+Js(2.0)))&Js(255.0))))&Js(95.0))))
                            # update
                            var.put('h', Js(3.0), '+')
                        ((var.get('h')==var.get('m')) and PyJsComma(var.put('r', var.get('s')(var.get('d')), '+'),var.put('g', (Js(3.0)*var.get('l')), '+')))
                    break
                # update
                var.put('l',Js(var.get('l').to_number())-Js(1))
            ((Js(0.0)==var.get('d')) and PyJsComma(var.put('r', var.get('s')(var.get('b')), '+'),var.put('g', Js(3.0), '+')))

    return var.get('r')
PyJsHoisted_h_.func_name = 'h'
var.put('h', PyJsHoisted_h_)
@Js
def PyJsHoisted_c_(c, b, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'f', 'c', 'b', 'e', 'd'])
    @Js
    def PyJsHoisted_d_(c, b, this, arguments, var=var):
        var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['c', 'h', 'u', 'm', 'r', 'b', 't'])
        var.put('t', ((((var.get('b')+Js('__x_countz_'))+var.get('e'))+var.get('c').get('length')) if (var.get('c').get('constructor')==var.get('Array')) else Js('')))
        for PyJsTemp in var.get('c'):
            var.put('h', PyJsTemp)
            if ((PyJsComma(Js(0.0), Js(None))!=var.put('m', var.get('c').get(var.get('h')))) and (var.get(u"null")!=var.get('m'))):
                if var.put('r', (Js('%')==(Js('')+var.get('h')).callprop('charAt', Js(0.0)))):
                    var.put('h', var.get('h').callprop('substr', Js(1.0)))
                var.put('u', (var.get('b')+(((Js('d') if (Js('')==var.get('b')) else Js('_'))+var.get('h')) if (Js(0.0)!=var.get('h')) else Js(''))))
                def PyJs_LONG_0_(var=var):
                    return ((var.get('t')+(((Js('') if (Js('')==var.get('t')) else var.get('f'))+(Js('') if (var.get('m').get('constructor')==var.get('Array')) else (((var.get('u')+var.get('e'))+Js('1'))+var.get('f'))))+var.get('d')(var.get('m'), var.get('u')))) if (var.get('m',throw=False).typeof()==var.get('q')) else (var.get('t')+((((Js('') if (Js('')==var.get('t')) else var.get('f'))+var.get('u'))+var.get('e'))+(var.get('m') if var.get('r') else var.get('g')((Js('')+var.get('m')), var.get('l'))))))
                ((Js('function')!=var.get('m',throw=False).typeof()) and var.put('t', PyJs_LONG_0_()))
        return var.get('t')
    PyJsHoisted_d_.func_name = 'd'
    var.put('d', PyJsHoisted_d_)
    pass
    var.put('e', (Js('-') if (Js('-')==var.get('b')) else Js('=')))
    var.put('f', (Js('&') if (Js('=')==var.get('e')) else Js('-')))
    var.put('l', (Js('_') if (Js('-')==var.get('b')) else Js('%')))
    return var.get('d')(var.get('c'), Js(''), var.get('b'))
PyJsHoisted_c_.func_name = 'c'
var.put('c', PyJsHoisted_c_)
@Js
def PyJsHoisted_l_(c, b, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'c', 'd'])
    @Js
    def PyJsHoisted_d_(c, b, e, this, arguments, var=var):
        var = Scope({'c':c, 'b':b, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'f', 'c', 'h', 'm', 'g', 'r', 'b', 'e'])
        var.put('m', (var.get('c').get('constructor')==var.get('Array')))
        var.put('r', (((((Js('<input type="hidden" name="')+var.get('b'))+Js('__x_countz_" value="'))+var.get('c').get('length'))+Js('"/>\r\n')) if var.get('m') else Js('')))
        for PyJsTemp in var.get('c'):
            var.put('g', PyJsTemp)
            if ((PyJsComma(Js(0.0), Js(None))!=var.put('f', var.get('c').get(var.get('g')))) and (var.get(u"null")!=var.get('f'))):
                def PyJs_LONG_1_(var=var):
                    return ((var.get('r')+(((Js('<div style="border:1px solid #00ffff;padding:2px;"><br/>\r\n')+(Js('') if (Js(0.0)==var.get('g')) else ((Js('<input type="hidden" name="')+var.get('l'))+Js('" value="1"/>\r\n'))))+var.get('d')(var.get('f'), var.get('l'), var.get('h')))+Js('</div>\r\n'))) if (var.get('f',throw=False).typeof()==var.get('q')) else (var.get('r')+((((((Js('<label>')+var.get('h'))+Js(':</label><input type="text" name="'))+var.get('l'))+Js('" value="'))+var.get('f'))+Js('"/><br/>'))))
                PyJsComma(PyJsComma(var.put('l', (var.get('b')+(((Js('d') if (Js('')==var.get('b')) else Js('_'))+var.get('g')) if (Js(0.0)!=var.get('g')) else Js('')))),var.put('h', ((Js('')+var.get('e'))+(((Js('[')+var.get('g'))+Js(']')) if var.get('m') else ((Js('') if (Js('')==var.get('e')) else Js('.'))+var.get('g')))))),var.put('r', PyJs_LONG_1_()))
        return var.get('r')
    PyJsHoisted_d_.func_name = 'd'
    var.put('d', PyJsHoisted_d_)
    pass
    return ((((Js('<form action="')+var.get('b'))+Js('" method="get" style="border:2px solid blue;padding:1px;"><button id="submit" type="submit">提交</button><br/>'))+var.get('d')(var.get('c'), Js(''), Js('')))+Js('</form>'))
PyJsHoisted_l_.func_name = 'l'
var.put('l', PyJsHoisted_l_)
@Js
def PyJsHoisted_m_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'f', 'c', 'h', 'g', 'r', 'b', 'e', 'd'])
    if var.get('c'):
        var.put('f', Js(0.0))
        var.put('h', (var.get('c').get('constructor')==var.get('Array')))
        var.put('r', (Js('[') if var.get('h') else Js('{')))
        for PyJsTemp in var.get('c'):
            var.put('b', PyJsTemp)
            while 1:
                SWITCHED = False
                CONDITION = (PyJsComma(PyJsComma(var.put('d', var.get('c').get(var.get('b'))),var.put('r', ((Js('') if (Js(0.0)==(var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1))) else Js(','))+(Js('') if var.get('h') else (var.get('b')+Js(':')))), '+')),var.get('d',throw=False).typeof()))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('number')):
                    SWITCHED = True
                    var.put('r', var.get('d'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('object')):
                    SWITCHED = True
                    var.put('r', var.get('m')(var.get('d')), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('string')):
                    SWITCHED = True
                    var.put('r', Js('"'), '+')
                    var.put('e', Js(0.0))
                    #for JS loop
                    var.put('l', var.get('d').get('length'))
                    while (var.get('e')<var.get('l')):
                        PyJsComma(var.put('g', var.get('d').callprop('charAt', var.get('e'))),var.put('r', ((Js('\\n') if (Js('\n')==var.get('g')) else (Js('\\r') if (Js('\r')==var.get('g')) else var.get('g'))) if ((Js('"')!=var.get('g')) and (Js('\\')!=var.get('g'))) else (Js('\\')+var.get('g'))), '+'))
                        # update
                        var.put('e',Js(var.get('e').to_number())+Js(1))
                    var.put('r', Js('"'), '+')
                SWITCHED = True
                break
        return (var.get('r')+(Js(']') if var.get('h') else Js('}')))
    return Js('')
PyJsHoisted_m_.func_name = 'm'
var.put('m', PyJsHoisted_m_)
var.put('mcodec', var.get(u"null"))
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.put('q', Js('object'))
var.put('s', var.get('String').get('fromCharCode'))
@Js
def PyJs_anonymous_2_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    try:
        return var.get('eval')(((Js('(')+var.get('a'))+Js(')')))
    except PyJsException as PyJsTempException:
        PyJsHolder_63_23186934 = var.own.get('c')
        var.force_own_put('c', PyExceptionToJs(PyJsTempException))
        try:
            return var.get(u"null")
        finally:
            if PyJsHolder_63_23186934 is not None:
                var.own['c'] = PyJsHolder_63_23186934
            else:
                del var.own['c']
            del PyJsHolder_63_23186934
PyJs_anonymous_2_._set_name('anonymous')
var.put('r', PyJs_anonymous_2_)
var.put('t', Js([Js(0.0), Js(192.0), Js(224.0), Js(240.0), Js(248.0), Js(252.0)]))
var.put('v', Js('0123456789abcdef'))
var.put('u', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='))
var.put('A', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-'))
var.put('C', Js({}))
var.put('B', Js([Js([Js('&'), Js('&amp;')]), Js([Js('\\n'), Js('&#10;')]), Js([Js('\\r'), Js('&#13;')]), Js([Js('\\t'), Js('&#9;')]), Js([Js('`'), Js('&#96;')]), Js([Js("'"), Js('&#39;')]), Js([Js('"'), Js('&quot;')]), Js([Js(' '), Js('&nbsp;')]), Js([Js('<'), Js('&lt;')]), Js([Js('>'), Js('&gt;')])]))
var.put('K', Js([Js({'s':JsRegExp('/\\[img\\]([^\\]]*)\\[\\/img\\]/gi'),'d':Js('<img src="$1" border="0"/>')}), Js({'s':JsRegExp('/\\[flash\\]([^\\]]*)\\[\\/flash\\]/gi'),'d':Js('<embed type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" quality="heigh" src="$1"/></embed>')}), Js({'s':JsRegExp('/\\[url=([^\\]]*)\\]([^\\]]*)\\[\\/url\\]/gi'),'d':Js('<a href="$1" target="_blank">$2</a>')}), Js({'s':JsRegExp('/\\[url\\]([^\\]]*)\\[\\/url\\]/gi'),'d':Js('<a href="$1" target="_blank">$1</a>')}), Js({'s':JsRegExp('/\\[email=([^\\]]*)\\]([^\\]]*)\\[\\/email\\]/gi'),'d':Js('<a href="mailto:$1">$2</a>')}), Js({'s':JsRegExp('/\\[email\\]([^\\]]*)\\[\\/email\\]/gi'),'d':Js('<a href="mailto:$1">$1</a>')}), Js({'s':JsRegExp('/\\[color=([^\\]]*)\\]([^\\]]*)\\[\\/color\\]/gi'),'d':Js('<font color="$1">$2</font>')}), Js({'s':JsRegExp('/\\[face=([^\\]]*)\\]([^\\]]*)\\[\\/face\\]/gi'),'d':Js('<font face="$1">$2</font>')}), Js({'s':JsRegExp('/\\[size=1\\]([^\\]]*)\\[\\/size\\]/gi'),'d':Js('<font size="1">$1</font>')}), Js({'s':JsRegExp('/\\[size=2\\]([^\\]]*)\\[\\/size\\]/gi'),'d':Js('<font size="2">$1</font>')}), Js({'s':JsRegExp('/\\[size=3\\]([^\\]]*)\\[\\/size\\]/gi'),'d':Js('<font size="3">$1</font>')}), Js({'s':JsRegExp('/\\[size=4\\]([^\\]]*)\\[\\/size\\]/gi'),'d':Js('<font size="4">$1</font>')}), Js({'s':JsRegExp('/\\[align=([^\\]]*)\\]([^]]*)\\[\\/face\\]/gi'),'d':Js('<align="$1">$2</align>')}), Js({'s':JsRegExp('/\\[fly\\]([^\\]]*)\\[\\/fly\\]/gi'),'d':Js('<marquee>$1</marquee>')}), Js({'s':JsRegExp('/\\[b\\]([^\\]]*)\\[\\/b\\]/gi'),'d':Js('<b>$1</b>')}), Js({'s':JsRegExp('/\\[i\\]([^\\]]*)\\[\\/i\\]/gi'),'d':Js('<i>$1</i>')}), Js({'s':JsRegExp('/\\[u\\]([^\\]]*)\\[\\/u\\]/gi'),'d':Js('<u>$1</u>')}), Js({'s':JsRegExp('/\\[code\\]([^\\]]*)\\[\\/code\\]/gi'),'d':Js('<pre><font size="2" face="Verdana,Arial">$1</font></pre>')}), Js({'s':JsRegExp('/\\[list\\]([^\\]]*)\\[\\/list\\]/gi'),'d':Js('<ul>$1</ul>')}), Js({'s':JsRegExp('/\\[list=1\\]([^\\]]*)\\[\\/list\\]/gi'),'d':Js('<ol type="1">$1</ol>')}), Js({'s':JsRegExp('/\\[list=a\\]([^\\]]*)\\[\\/list\\]/gi'),'d':Js('<ol type="a">$1</ol>')}), Js({'s':JsRegExp('/\\[\\*\\]([^\\]]*)\\[\\/\\*\\]/gi'),'d':Js('<li>$1</li>')}), Js({'s':JsRegExp('/\\[quote\\]([^\\]]*)\\[\\/quote\\]/gi'),'d':Js('<blockquote>$1</blockquote>')})]))
#for JS loop
var.put('F', Js(0.0))
while (Js(21.0)>var.get('F')):
    var.get('C').put(Js('\x00\t\n\r"\\\' #%&+-_./:;=?@').callprop('charAt', var.get('F')), Js(1.0))
    # update
    var.put('F',Js(var.get('F').to_number())+Js(1))
def PyJs_LONG_15_(var=var):
    @Js
    def PyJs_anonymous_3_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'f', 'c', 'h', 'm', 'g', 'a', 'b', 'e', 'd'])
        if var.get('a'):
            #for JS loop
            var.put('c', Js([]))
            var.put('b', Js(0.0))
            while (var.get('b')<var.get('A').get('length')):
                var.get('c').put(var.get('A').callprop('charAt', var.get('b')), var.get('b'))
                # update
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
            var.put('l', var.get('a').get('length'))
            var.put('h', var.get('l'))
            ((Js('-')==var.get('a').callprop('charAt', (var.get('l')-Js(1.0)))) and var.put('h', Js(4.0), '-'))
            #for JS loop
            var.put('m', Js([]))
            var.put('b', Js(0.0))
            while (var.get('b')<var.get('h')):
                def PyJs_LONG_4_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('d', var.get('c').get(var.get('a').callprop('charAt', var.get('b')))),var.put('e', var.get('c').get(var.get('a').callprop('charAt', (var.get('b')+Js(1.0)))))),var.put('g', var.get('c').get(var.get('a').callprop('charAt', (var.get('b')+Js(2.0)))))),var.put('f', var.get('c').get(var.get('a').callprop('charAt', (var.get('b')+Js(3.0)))))),var.put('d', ((var.get('d')<<Js(2.0))|(var.get('e')>>Js(4.0))))),var.put('e', ((var.get('e')<<Js(4.0))|(var.get('g')>>Js(2.0))))),var.put('g', ((var.get('g')<<Js(6.0))|var.get('f')))),var.get('m').callprop('push', (var.get('d')&Js(255.0)))),var.get('m').callprop('push', (var.get('e')&Js(255.0)))),var.get('m').callprop('push', (var.get('g')&Js(255.0))))
                PyJs_LONG_4_()
                # update
                var.put('b', Js(4.0), '+')
            def PyJs_LONG_5_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('d', var.get('c').get(var.get('a').callprop('charAt', var.get('b')))),var.put('e', var.get('c').get(var.get('a').callprop('charAt', (var.get('b')+Js(1.0)))))),var.put('g', var.get('a').callprop('charAt', (var.get('b')+Js(2.0))))),var.get('m').callprop('push', (((var.get('d')<<Js(2.0))|(var.get('e')>>Js(4.0)))&Js(255.0)))),((Js('-')!=var.get('g')) and PyJsComma(var.put('g', var.get('c').get(var.get('g'))),var.get('m').callprop('push', (((var.get('e')<<Js(4.0))|(var.get('g')>>Js(2.0)))&Js(255.0))))))
            ((var.get('h')!=var.get('l')) and PyJs_LONG_5_())
            return var.get('m')
    PyJs_anonymous_3_._set_name('anonymous')
    @Js
    def PyJs_anonymous_6_(a, c, this, arguments, var=var):
        var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'f', 'c', 'h', 'm', 'g', 'a', 'b', 'e', 'd'])
        #for JS loop
        var.put('f', Js(0.0))
        var.put('l', Js(''))
        var.put('h', var.get('a').get('length'))
        var.put('m', (var.get('A') if var.get('c') else var.get('u')))
        while (var.get('f')<var.get('h')):
            #for JS loop
            var.put('d', Js(0.0))
            while ((Js(24.0)>var.get('d')) and (var.get('f')<var.get('h'))):
                var.put('b', ((var.get('b')<<Js(8.0))+var.get('a').get(var.get('f'))))
                # update
                PyJsComma(var.put('d', Js(8.0), '+'),(var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1)))
            #for JS loop
            var.put('g', Js(0.0))
            while (Js(24.0)>var.get('g')):
                PyJsComma(var.put('e', ((var.get('d')-var.get('g'))-Js(6.0))),var.put('l', (var.get('m').callprop('charAt', ((var.get('b')<<(-var.get('e'))) if (Js(0.0)>var.get('e')) else (var.get('b')>>var.get('e')))) if (var.get('g')<var.get('d')) else Js('')), '+'))
                # update
                PyJsComma(var.put('g', Js(6.0), '+'),var.put('b', ((Js(1.0)<<(var.get('d')-var.get('g')))-Js(1.0)), '&'))

        return var.get('l')
    PyJs_anonymous_6_._set_name('anonymous')
    @Js
    def PyJs_anonymous_7_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'f', 'a', 'q', 'c', 'u', 'm', 'g', 'r', 'b', 'e', 'd'])
        var.put('c', Js({}))
        var.put('m', var.get('a').get('length'))
        var.put('r', (Js('-') if ((Js(0.0)<var.get('m')) and (Js('-')==var.get('a').callprop('charAt', Js(0.0)))) else Js('=')))
        var.put('q', (Js('-') if (Js('-')==var.get('r')) else Js('&')))
        var.put('u', (Js('_') if (Js('-')==var.get('q')) else Js('%')))
        #for JS loop
        var.put('l', Js(1.0))
        while (var.get('l')<var.get('m')):
            #for JS loop
            var.put('d', var.get('l'))
            while (((var.get('l')<var.get('m')) and (var.get('r')!=var.put('b', var.get('a').callprop('charAt', var.get('l'))))) and (var.get('b')!=var.get('q'))):
                pass
                # update
                var.put('l',Js(var.get('l').to_number())+Js(1))
            var.put('g', (var.get('l')-var.get('d')))
            #for JS loop
            var.put('e', var.put('l', (Js(1.0) if ((var.get('l')<var.get('m')) and (var.get('r')==var.get('b'))) else Js(0.0)), '+'))
            while ((var.get('l')<var.get('m')) and (var.get('q')!=var.get('a').callprop('charAt', var.get('l')))):
                pass
                # update
                var.put('l',Js(var.get('l').to_number())+Js(1))
            var.put('f', (var.get('l')-var.get('e')))
            (((Js(0.0)<var.get('g')) and (Js(0.0)<var.get('f'))) and var.get('c').put(var.get('a').callprop('substr', var.get('d'), var.get('g')), var.get('h')(var.get('a').callprop('substr', var.get('e'), var.get('f')), var.get('u'))))
            # update
            var.put('l',Js(var.get('l').to_number())+Js(1))
        return var.get('c')
    PyJs_anonymous_7_._set_name('anonymous')
    @Js
    def PyJs_anonymous_8_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'b', 'e', 'd'])
        var.put('d', var.get('a').callprop('indexOf', Js('(')))
        var.put('e', var.get('a').callprop('lastIndexOf', Js(')')))
        (((Js(0.0)<var.get('d')) and (var.get('e')>var.get('d'))) and var.put('a', var.get('a').callprop('substring', (var.get('d')+Js(1.0)), var.get('e'))))
        return var.get('c')(var.get('r')(var.get('a')), var.get('b'))
    PyJs_anonymous_8_._set_name('anonymous')
    @Js
    def PyJs_anonymous_9_(a, c, this, arguments, var=var):
        var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'b', 'c', 'd'])
        var.put('b', var.get('a').callprop('indexOf', Js('(')))
        var.put('d', var.get('a').callprop('lastIndexOf', Js(')')))
        (((Js(0.0)<var.get('b')) and (var.get('d')>var.get('b'))) and var.put('a', var.get('a').callprop('substring', (var.get('b')+Js(1.0)), var.get('d'))))
        return var.get('l')(var.get('r')(var.get('a')), var.get('c'))
    PyJs_anonymous_9_._set_name('anonymous')
    @Js
    def PyJs_anonymous_10_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['c', 'a'])
        #for JS loop
        var.put('c', Js(0.0))
        while (var.get('c')<var.get('B').get('length')):
            var.put('a', var.get('a').callprop('replace', var.get('RegExp')(var.get('B').get(var.get('c')).get('0'), Js('g')), var.get('B').get(var.get('c')).get('1')))
            # update
            var.put('c',Js(var.get('c').to_number())+Js(1))
        return var.get('a')
    PyJs_anonymous_10_._set_name('anonymous')
    @Js
    def PyJs_anonymous_11_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['c', 'a'])
        #for JS loop
        var.put('c', (var.get('B').get('length')-Js(1.0)))
        while (Js(0.0)<=var.get('c')):
            var.put('a', var.get('a').callprop('replace', var.get('RegExp')(var.get('B').get(var.get('c')).get('1'), Js('g')), var.get('B').get(var.get('c')).get('0')))
            # update
            var.put('c',Js(var.get('c').to_number())-Js(1))
        return var.get('a')
    PyJs_anonymous_11_._set_name('anonymous')
    @Js
    def PyJs_anonymous_12_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['b', 'c', 'a'])
        #for JS loop
        var.put('b', var.get('K').get('length'))
        while (Js(0.0)<=var.get('b')):
            PyJsComma(var.put('c', var.get('K').get(var.get('b'))),var.put('a', var.get('a').callprop('replace', var.get('c').get('s'), var.get('c').get('d'))))
            # update
            var.put('b',Js(var.get('b').to_number())-Js(1))
        return var.get('a')
    PyJs_anonymous_12_._set_name('anonymous')
    @Js
    def PyJs_anonymous_13_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['b', 'c', 'a'])
        var.put('b', Js(''))
        #for JS loop
        var.put('c', Js(0.0))
        while (var.get('c')<var.get('a').get('length')):
            var.put('b', ((Js('%') if (Js(0.0)==(Js(1.0)&var.get('c'))) else Js(''))+var.get('a').callprop('charAt', var.get('c'))), '+')
            # update
            var.put('c',Js(var.get('c').to_number())+Js(1))
        return var.get('b')
    PyJs_anonymous_13_._set_name('anonymous')
    @Js
    def PyJs_anonymous_14_(a, c, e, g, f, l, h, m, this, arguments, var=var):
        var = Scope({'a':a, 'c':c, 'e':e, 'g':g, 'f':f, 'l':l, 'h':h, 'm':m, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'f', 'g', 'c', 'h', 'm', 'a', 'r', 'e'])
        var.put('a', var.get('d')(var.get('a')))
        var.put('r', (var.get('d')(var.get('c')) if var.get('c') else Js('')))
        var.put('c', (var.get('d')(var.get('g')) if var.get('c') else Js('')))
        var.put('l', (var.get('d')((Js('0x')+var.get('h').callprop(var.get('m'), var.get('l')))) if var.get('l') else Js('')))
        var.put('f', (((((var.get('s')((Js(64.0)+var.get('a').get('length')))+var.get('a')) if var.get('a') else Js(''))+((var.get('s')((Js(96.0)+var.get('r').get('length')))+var.get('r')) if var.get('r') else Js('')))+((var.get('s')((Js(128.0)+var.get('c').get('length')))+var.get('c')) if var.get('c') else Js('')))+((var.get('s')((Js(160.0)+var.get('f').get('length')))+var.get('f')) if var.get('f') else Js(''))))
        var.put('e', ((var.get('f')+((var.get('s')((Js(0.0)+var.get('e').get('length')))+var.get('e')) if var.get('e') else Js('')))+((var.get('s')((Js(0.0)+var.get('l').get('length')))+var.get('l')) if var.get('l') else Js(''))))
        var.put('s_md5', var.get('d')((Js('0x')+var.get('h').callprop(var.get('m'), var.get('e')))))
        return var.get('b')(((var.get('s')((Js(32.0)+var.get('s_md5').get('length')))+var.get('s_md5'))+var.get('f')), Js(1.0))
    PyJs_anonymous_14_._set_name('anonymous')
    return var.put('mcodec', Js({'magic':Js('mcodec'),'str_2_b64':var.get('b'),'b64_2_binary':PyJs_anonymous_3_,'binary_2_b64':PyJs_anonymous_6_,'str_2_uri_param':var.get('g'),'uri_param_2_str':var.get('h'),'uri_2_obj':PyJs_anonymous_7_,'obj_2_url':var.get('c'),'json_txt_2_url':PyJs_anonymous_8_,'obj_2_form':var.get('l'),'json_txt_2_form':PyJs_anonymous_9_,'obj_2_str':var.get('m'),'str_2_html':PyJs_anonymous_10_,'html_2_str':PyJs_anonymous_11_,'ubb_2_html':PyJs_anonymous_12_,'hex_2_uri_param':PyJs_anonymous_13_,'nid':PyJs_anonymous_14_}))
PyJs_LONG_15_()
pass


# Add lib to the module scope
mcodec = var.to_python()