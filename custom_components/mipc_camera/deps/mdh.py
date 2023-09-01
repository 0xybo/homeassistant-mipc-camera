__all__ = ['mdh']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['pb', 'C', 'ha', 'l', 'G', 'qb', 'Xa', 'u', 'g', 'T', 'b', 'B', 'e', 'L', 'H', 'N', 'z', 'K', 'A', 't', 'Ea', 'd', 's', 'Cb', 'q', 'c', 'I', 'v', 'h', 'm', 'F', 'M', 'r'])
@Js
def PyJsHoisted_e_(c, b, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'e', 'c', 'd'])
    #for JS loop
    var.put('d', Js(1.0))
    var.put('e', Js(0.0))
    while 1:
        if (Js(1.0)==var.get('c')):
            return var.get('d')
        if (Js(0.0)==var.get('c')):
            return Js(0.0)
        var.put('e', (var.get('d')*var.get('Math').callprop('floor', (var.get('b')/var.get('c')))), '-')
        var.put('b', var.get('c'), '%')
        if (Js(1.0)==var.get('b')):
            return var.get('e')
        if (Js(0.0)==var.get('b')):
            return Js(0.0)
        var.put('d', (var.get('e')*var.get('Math').callprop('floor', (var.get('c')/var.get('b')))), '-')
        var.put('c', var.get('b'), '%')

PyJsHoisted_e_.func_name = 'e'
var.put('e', PyJsHoisted_e_)
@Js
def PyJsHoisted_d_(a, c, b, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['g', 'c', 'a', 'b', 'e', 'd'])
    var.put('e', var.get('a').get('length'))
    var.put('g', var.get('c').get('length'))
    var.put('k', ((var.get('e')+var.get('b')) if ((var.get('e')+var.get('b'))<var.get('g')) else var.get('g')))
    #for JS loop
    var.put('d', ((var.get('g')-Js(1.0))-var.get('b')))
    while ((var.get('d')<var.get('e')) and (Js(0.0)<=var.get('d'))):
        if (Js(0.0)<var.get('a').get(var.get('d'))):
            return Js(1.0)
        # update
        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('d', ((var.get('e')-Js(1.0))+var.get('b')))
    while (var.get('d')<var.get('g')):
        if (Js(0.0)<var.get('c').get(var.get('d'))):
            return Js(0.0)
        # update
        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('d', (var.get('k')-Js(1.0)))
    while (var.get('d')>=var.get('b')):
        if (var.get('a').get((var.get('d')-var.get('b')))>var.get('c').get(var.get('d'))):
            return Js(1.0)
        if (var.get('a').get((var.get('d')-var.get('b')))<var.get('c').get(var.get('d'))):
            break
        # update
        (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
    return Js(0.0)
PyJsHoisted_d_.func_name = 'd'
var.put('d', PyJsHoisted_d_)
@Js
def PyJsHoisted_b_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b', 'c', 'd'])
    var.put('d', (var.get('a').get('length') if (var.get('a').get('length')<var.get('c').get('length')) else var.get('c').get('length')))
    #for JS loop
    var.put('b', var.get('a').get('length'))
    while (var.get('b')<var.get('c').get('length')):
        if var.get('c').get(var.get('b')):
            return Js(0.0)
        # update
        (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('b', var.get('c').get('length'))
    while (var.get('b')<var.get('a').get('length')):
        if var.get('a').get(var.get('b')):
            return Js(1.0)
        # update
        (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('b', (var.get('d')-Js(1.0)))
    while (Js(0.0)<=var.get('b')):
        if (var.get('a').get(var.get('b'))>var.get('c').get(var.get('b'))):
            return Js(1.0)
        if (var.get('a').get(var.get('b'))<var.get('c').get(var.get('b'))):
            break
        # update
        (var.put('b',Js(var.get('b').to_number())-Js(1))+Js(1))
    return Js(0.0)
PyJsHoisted_b_.func_name = 'b'
var.put('b', PyJsHoisted_b_)
@Js
def PyJsHoisted_g_(c, b, d, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'c', 'd'])
    var.put('b', (var.get('Math').callprop('ceil', (var.get('b')/var.get('z')))+Js(1.0)))
    var.put('buff', var.get('Array').create((var.get('d') if (var.get('d')>var.get('b')) else var.get('b'))))
    var.get('r')(var.get('buff'), var.get('c'))
    return var.get('buff')
PyJsHoisted_g_.func_name = 'g'
var.put('g', PyJsHoisted_g_)
@Js
def PyJsHoisted_h_(a, c, b, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'C', 'q', 'c', 'h', 'u', 'm', 'a', 'r', 'b', 't', 'e', 'd'])
    var.put('h', var.get('a').get('length'))
    if ((-Js(1.0))==var.get('c')):
        #for JS loop
        var.put('l', var.get('Array').create(Js(0.0)))
        while 1:
            var.put('c', var.get('Array').create((var.get('l').get('length')+Js(1.0))))
            #for JS loop
            var.put('e', Js(0.0))
            while (var.get('e')<var.get('l').get('length')):
                var.get('c').put((var.get('e')+Js(1.0)), var.get('l').get(var.get('e')))
                # update
                (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
            var.get('c').put('0', var.get('parseInt')(var.get('a'), Js(10.0)))
            var.put('l', var.get('c'))
            var.put('d', var.get('a').callprop('indexOf', Js(','), Js(0.0)))
            if (Js(1.0)>var.get('d')):
                break
            var.put('a', var.get('a').callprop('substring', (var.get('d')+Js(1.0))))
            if (Js(0.0)==var.get('a').get('length')):
                break

        return (PyJsComma(PyJsComma(var.put('c', var.get('Array').create(var.get('b'))),var.get('s')(var.get('c'), var.get('l'))),var.get('c')) if (var.get('l').get('length')<var.get('b')) else var.get('l'))
    var.put('l', var.get('g')(Js(0.0), (var.get('c')*var.get('h')), Js(0.0)))
    #for JS loop
    var.put('e', Js(0.0))
    while (var.get('e')<var.get('h')):
        var.put('d', var.get('M').callprop('indexOf', var.get('a').callprop('substring', var.get('e'), (var.get('e')+Js(1.0))), Js(0.0)))
        (((Js(36.0)>=var.get('c')) and (Js(36.0)<=var.get('d'))) and var.put('d', Js(26.0), '-'))
        if ((var.get('d')>=var.get('c')) or (Js(0.0)>var.get('d'))):
            break
        var.put('m', var.get('l'))
        var.put('r', var.get('c'))
        var.put('q', PyJsComma(Js(0.0), Js(None)))
        var.put('u', PyJsComma(Js(0.0), Js(None)))
        var.put('t', PyJsComma(Js(0.0), Js(None)))
        var.put('C', PyJsComma(Js(0.0), Js(None)))
        if var.get('r'):
            var.put('u', var.get('m').get('length'))
            #for JS loop
            var.put('q', var.put('t', Js(0.0)))
            while (var.get('q')<var.get('u')):
                PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('t', (var.get('m').get(var.get('q'))*var.get('r')), '+'),var.put('C', Js(0.0))),((Js(0.0)>var.get('t')) and PyJsComma(var.put('C', (-(var.get('t')>>var.get('z')))),var.put('t', (var.get('C')*var.get('N')), '+')))),var.get('m').put(var.get('q'), (var.get('t')&var.get('H')))),var.put('t', ((var.get('t')>>var.get('z'))-var.get('C'))))
                # update
                (var.put('q',Js(var.get('q').to_number())+Js(1))-Js(1))
        var.put('m', var.get('l'))
        var.put('t', var.put('u', var.put('q', var.put('r', PyJsComma(Js(0.0), Js(None))))))
        var.get('m').put('0', var.get('d'), '+')
        var.put('q', var.get('m').get('length'))
        #for JS loop
        var.put('r', var.put('u', Js(0.0)))
        def PyJs_LONG_0_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('u', var.get('m').get(var.get('r')), '+'),var.put('t', Js(0.0))),((Js(0.0)>var.get('u')) and PyJsComma(var.put('t', (-(var.get('u')>>var.get('z')))),var.put('u', (var.get('t')*var.get('N')), '+')))),var.get('m').put(var.get('r'), (var.get('u')&var.get('H')))),var.put('u', ((var.get('u')>>var.get('z'))-var.get('t')))),var.get('u').neg()).neg()
        while ((var.get('r')<var.get('q')) and PyJs_LONG_0_()):
            pass
            # update
            (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
        # update
        (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('h', var.get('l').get('length'))
    while ((Js(0.0)<var.get('h')) and var.get('l').get((var.get('h')-Js(1.0))).neg()):
        pass
        # update
        (var.put('h',Js(var.get('h').to_number())-Js(1))+Js(1))
    var.put('h', (var.get('b') if (var.get('b')>(var.get('h')+Js(1.0))) else (var.get('h')+Js(1.0))))
    var.put('c', var.get('Array').create(var.get('h')))
    var.put('a', (var.get('h') if (var.get('h')<var.get('l').get('length')) else var.get('l').get('length')))
    #for JS loop
    var.put('e', Js(0.0))
    while (var.get('e')<var.get('a')):
        var.get('c').put(var.get('e'), var.get('l').get(var.get('e')))
        # update
        (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    #for JS loop

    while (var.get('e')<var.get('h')):
        var.get('c').put(var.get('e'), Js(0.0))
        # update
        (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    return var.get('c')
PyJsHoisted_h_.func_name = 'h'
var.put('h', PyJsHoisted_h_)
@Js
def PyJsHoisted_c_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'c', 'a'])
    pass
    if (var.get('a').get('0')!=var.get('c')):
        return Js(0.0)
    #for JS loop
    var.put('b', Js(1.0))
    while (var.get('b')<var.get('a').get('length')):
        if var.get('a').get(var.get('b')):
            return Js(0.0)
        # update
        (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    return Js(1.0)
PyJsHoisted_c_.func_name = 'c'
var.put('c', PyJsHoisted_c_)
@Js
def PyJsHoisted_l_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a'])
    pass
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('a').get('length')):
        if var.get('a').get(var.get('c')):
            return Js(0.0)
        # update
        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
    return Js(1.0)
PyJsHoisted_l_.func_name = 'l'
var.put('l', PyJsHoisted_l_)
@Js
def PyJsHoisted_m_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b', 'c', 'd'])
    var.put('d', Js(''))
    (var.put('Ea', var.get('q')(var.get('a'))) if (var.get('Ea').get('length')!=var.get('a').get('length')) else var.get('s')(var.get('Ea'), var.get('a')))
    if ((-Js(1.0))==var.get('c')):
        #for JS loop
        var.put('b', (var.get('a').get('length')-Js(1.0)))
        while (Js(0.0)<var.get('b')):
            var.put('d', (var.get('a').get(var.get('b'))+Js(',')), '+')
            # update
            (var.put('b',Js(var.get('b').to_number())-Js(1))+Js(1))
        var.put('d', var.get('a').get('0'), '+')
    else:
        #for JS loop

        while var.get('l')(var.get('Ea')).neg():
            PyJsComma(var.put('b', var.get('u')(var.get('Ea'), var.get('c'))),var.put('d', (var.get('M').callprop('substring', var.get('b'), (var.get('b')+Js(1.0)))+var.get('d'))))

    ((Js(0.0)==var.get('d').get('length')) and var.put('d', Js('0')))
    return var.get('d')
PyJsHoisted_m_.func_name = 'm'
var.put('m', PyJsHoisted_m_)
@Js
def PyJsHoisted_q_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('buff', var.get('Array').create(var.get('a').get('length')))
    var.get('s')(var.get('buff'), var.get('a'))
    return var.get('buff')
PyJsHoisted_q_.func_name = 'q'
var.put('q', PyJsHoisted_q_)
@Js
def PyJsHoisted_s_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b', 'c', 'd'])
    var.put('d', (var.get('a').get('length') if (var.get('a').get('length')<var.get('c').get('length')) else var.get('c').get('length')))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('d')):
        var.get('a').put(var.get('b'), var.get('c').get(var.get('b')))
        # update
        (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('b', var.get('d'))
    while (var.get('b')<var.get('a').get('length')):
        var.get('a').put(var.get('b'), Js(0.0))
        # update
        (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
PyJsHoisted_s_.func_name = 's'
var.put('s', PyJsHoisted_s_)
@Js
def PyJsHoisted_r_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b', 'c', 'd'])
    pass
    var.put('d', var.get('c'))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('a').get('length')):
        PyJsComma(var.get('a').put(var.get('b'), (var.get('d')&var.get('H'))),var.put('d', var.get('z'), '>>'))
        # update
        (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
PyJsHoisted_r_.func_name = 'r'
var.put('r', PyJsHoisted_r_)
@Js
def PyJsHoisted_t_(c, b, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'e', 'c', 'd'])
    var.put('e', var.get('Math').callprop('floor', (var.get('b')/var.get('z'))))
    if var.get('e'):
        #for JS loop
        var.put('d', Js(0.0))
        while (var.get('d')<(var.get('c').get('length')-var.get('e'))):
            var.get('c').put(var.get('d'), var.get('c').get((var.get('d')+var.get('e'))))
            # update
            (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
        #for JS loop

        while (var.get('d')<var.get('c').get('length')):
            var.get('c').put(var.get('d'), Js(0.0))
            # update
            (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
        var.put('b', var.get('z'), '%')
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<(var.get('c').get('length')-Js(1.0))):
        var.get('c').put(var.get('d'), (var.get('H')&((var.get('c').get((var.get('d')+Js(1.0)))<<(var.get('z')-var.get('b')))|(var.get('c').get(var.get('d'))>>var.get('b')))))
        # update
        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    var.get('c').put(var.get('d'), var.get('b'), '>>')
PyJsHoisted_t_.func_name = 't'
var.put('t', PyJsHoisted_t_)
@Js
def PyJsHoisted_v_(c, b, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'e', 'c', 'd'])
    var.put('e', var.get('Math').callprop('floor', (var.get('b')/var.get('z'))))
    if var.get('e'):
        #for JS loop
        var.put('d', var.get('c').get('length'))
        while (var.get('d')>=var.get('e')):
            var.get('c').put(var.get('d'), var.get('c').get((var.get('d')-var.get('e'))))
            # update
            (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
        #for JS loop

        while (Js(0.0)<=var.get('d')):
            var.get('c').put(var.get('d'), Js(0.0))
            # update
            (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
        var.put('b', var.get('z'), '%')
    if var.get('b'):
        #for JS loop
        var.put('d', (var.get('c').get('length')-Js(1.0)))
        while (Js(0.0)<var.get('d')):
            var.get('c').put(var.get('d'), (var.get('H')&((var.get('c').get(var.get('d'))<<var.get('b'))|(var.get('c').get((var.get('d')-Js(1.0)))>>(var.get('z')-var.get('b'))))))
            # update
            (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
        var.get('c').put(var.get('d'), (var.get('H')&(var.get('c').get(var.get('d'))<<var.get('b'))))
PyJsHoisted_v_.func_name = 'v'
var.put('v', PyJsHoisted_v_)
@Js
def PyJsHoisted_u_(c, b, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'e', 'c', 'd'])
    var.put('e', Js(0.0))
    #for JS loop
    var.put('d', (var.get('c').get('length')-Js(1.0)))
    while (Js(0.0)<=var.get('d')):
        PyJsComma(PyJsComma(var.put('e', ((var.get('e')*var.get('N'))+var.get('c').get(var.get('d')))),var.get('c').put(var.get('d'), var.get('Math').callprop('floor', (var.get('e')/var.get('b'))))),var.put('e', var.get('b'), '%'))
        # update
        (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
    return var.get('e')
PyJsHoisted_u_.func_name = 'u'
var.put('u', PyJsHoisted_u_)
@Js
def PyJsHoisted_A_(a, c, b, d, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'b':b, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'f', 'g', 'c', 'a', 'b', 'e', 'd'])
    pass
    var.put('f', (var.get('a').get('length') if (var.get('a').get('length')<(var.get('d')+var.get('c').get('length'))) else (var.get('d')+var.get('c').get('length'))))
    var.put('l', var.get('a').get('length'))
    var.put('g', Js(0.0))
    #for JS loop
    var.put('e', var.get('d'))
    while (var.get('e')<var.get('f')):
        PyJsComma(PyJsComma(var.put('g', (var.get('a').get(var.get('e'))+(var.get('b')*var.get('c').get((var.get('e')-var.get('d'))))), '+'),var.get('a').put(var.get('e'), (var.get('g')&var.get('H')))),var.put('g', var.get('z'), '>>'))
        # update
        (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('e', var.get('f'))
    while (var.get('g') and (var.get('e')<var.get('l'))):
        PyJsComma(PyJsComma(var.put('g', var.get('a').get(var.get('e')), '+'),var.get('a').put(var.get('e'), (var.get('g')&var.get('H')))),var.put('g', var.get('z'), '>>'))
        # update
        (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
PyJsHoisted_A_.func_name = 'A'
var.put('A', PyJsHoisted_A_)
@Js
def PyJsHoisted_C_(c, b, this, arguments, var=var):
    var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'f', 'p', 'C', 'c', 'h', 'u', 'm', 'F', 'g', 'b', 'B', 'e'])
    (var.put('pb', var.get('q')(var.get('c'))) if (var.get('pb').get('length')!=var.get('c').get('length')) else var.get('s')(var.get('pb'), var.get('c')))
    ((var.get('qb').get('length')!=var.get('c').get('length')) and var.put('qb', var.get('q')(var.get('c'))))
    var.put('e', var.get('qb'))
    var.get('s')(var.get('c'), var.get('pb'))
    #for JS loop
    var.put('f', var.get('b').get('length'))
    while (Js(0.0)==var.get('b').get((var.get('f')-Js(1.0)))):
        pass
        # update
        (var.put('f',Js(var.get('f').to_number())-Js(1))+Js(1))
    var.put('g', var.get('b').get((var.get('f')-Js(1.0))))
    #for JS loop
    var.put('u', Js(0.0))
    while var.get('g'):
        var.put('g', Js(1.0), '>>')
        # update
        (var.put('u',Js(var.get('u').to_number())+Js(1))-Js(1))
    var.put('u', (var.get('z')-var.get('u')))
    var.get('v')(var.get('b'), var.get('u'))
    var.get('v')(var.get('c'), var.get('u'))
    #for JS loop
    var.put('g', var.get('c').get('length'))
    while ((Js(0.0)==var.get('c').get((var.get('g')-Js(1.0)))) and (var.get('g')>var.get('f'))):
        pass
        # update
        (var.put('g',Js(var.get('g').to_number())-Js(1))+Js(1))
    #for JS loop
    var.get('r')(var.get('e'), Js(0.0))
    while var.get('d')(var.get('b'), var.get('c'), (var.get('g')-var.get('f'))).neg():
        var.put('l', var.get('c'))
        var.put('h', var.get('b'))
        var.put('m', (var.get('g')-var.get('f')))
        #for JS loop
        var.put('p', PyJsComma(Js(0.0), Js(None)))
        var.put('C', PyJsComma(Js(0.0), Js(None)))
        var.put('B', PyJsComma(Js(0.0), Js(None)))
        var.put('F', PyJsComma(Js(0.0), Js(None)))
        var.put('B', (var.get('l').get('length') if (var.get('l').get('length')<(var.get('m')+var.get('h').get('length'))) else (var.get('m')+var.get('h').get('length'))))
        var.put('F', var.get('l').get('length'))
        var.put('C', Js(0.0))
        var.put('p', var.get('m'))
        while (var.get('p')<var.get('B')):
            PyJsComma(PyJsComma(var.put('C', (var.get('l').get(var.get('p'))-var.get('h').get((var.get('p')-var.get('m')))), '+'),var.get('l').put(var.get('p'), (var.get('C')&var.get('H')))),var.put('C', var.get('z'), '>>'))
            # update
            (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('p', var.get('B'))
        while (var.get('C') and (var.get('p')<var.get('F'))):
            PyJsComma(PyJsComma(var.put('C', var.get('l').get(var.get('p')), '+'),var.get('l').put(var.get('p'), (var.get('C')&var.get('H')))),var.put('C', var.get('z'), '>>'))
            # update
            (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
        (var.get('e').put((var.get('g')-var.get('f')),Js(var.get('e').get((var.get('g')-var.get('f'))).to_number())+Js(1))-Js(1))

    #for JS loop
    var.put('g', Js(1.0), '-')
    while (var.get('g')>=var.get('f')):
        #for JS loop
        var.get('e').put((var.get('g')-var.get('f')), (var.get('H') if (var.get('c').get(var.get('g'))==var.get('b').get((var.get('f')-Js(1.0)))) else var.get('Math').callprop('floor', (((var.get('c').get(var.get('g'))*var.get('N'))+var.get('c').get((var.get('g')-Js(1.0))))/var.get('b').get((var.get('f')-Js(1.0)))))))
        while 1:
            def PyJs_LONG_1_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('h', ((var.get('b').get((var.get('f')-Js(2.0))) if (Js(1.0)<var.get('f')) else Js(0.0))*var.get('e').get((var.get('g')-var.get('f'))))),var.put('m', (var.get('h')>>var.get('z')))),var.put('h', var.get('H'), '&')),var.put('l', (var.get('m')+(var.get('e').get((var.get('g')-var.get('f')))*var.get('b').get((var.get('f')-Js(1.0))))))),var.put('m', (var.get('l')>>var.get('z')))),var.put('l', var.get('H'), '&')),(((var.get('h')>(var.get('c').get((var.get('g')-Js(2.0))) if (Js(1.0)<var.get('g')) else Js(0.0))) if (var.get('l')==var.get('c').get((var.get('g')-Js(1.0)))) else (var.get('l')>var.get('c').get((var.get('g')-Js(1.0))))) if (var.get('m')==var.get('c').get(var.get('g'))) else (var.get('m')>var.get('c').get(var.get('g')))))
            if PyJs_LONG_1_():
                (var.get('e').put((var.get('g')-var.get('f')),Js(var.get('e').get((var.get('g')-var.get('f'))).to_number())-Js(1))+Js(1))
            else:
                break

        var.get('A')(var.get('c'), var.get('b'), (-var.get('e').get((var.get('g')-var.get('f')))), (var.get('g')-var.get('f')))
        if ((var.get('c').get((var.get('c').get('length')-Js(1.0)))>>(var.get('z')-Js(1.0)))&Js(1.0)):
            var.put('l', var.get('c'))
            var.put('h', var.get('b'))
            var.put('m', (var.get('g')-var.get('f')))
            var.put('F', var.put('B', var.put('C', var.put('p', PyJsComma(Js(0.0), Js(None))))))
            var.put('B', (var.get('l').get('length') if (var.get('l').get('length')<(var.get('m')+var.get('h').get('length'))) else (var.get('m')+var.get('h').get('length'))))
            var.put('F', var.get('l').get('length'))
            var.put('C', Js(0.0))
            #for JS loop
            var.put('p', var.get('m'))
            while (var.get('p')<var.get('B')):
                PyJsComma(PyJsComma(var.put('C', (var.get('l').get(var.get('p'))+var.get('h').get((var.get('p')-var.get('m')))), '+'),var.get('l').put(var.get('p'), (var.get('C')&var.get('H')))),var.put('C', var.get('z'), '>>'))
                # update
                (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('p', var.get('B'))
            while (var.get('C') and (var.get('p')<var.get('F'))):
                PyJsComma(PyJsComma(var.put('C', var.get('l').get(var.get('p')), '+'),var.get('l').put(var.get('p'), (var.get('C')&var.get('H')))),var.put('C', var.get('z'), '>>'))
                # update
                (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
            (var.get('e').put((var.get('g')-var.get('f')),Js(var.get('e').get((var.get('g')-var.get('f'))).to_number())-Js(1))+Js(1))
        # update
        (var.put('g',Js(var.get('g').to_number())-Js(1))+Js(1))
    var.get('t')(var.get('b'), var.get('u'))
    var.get('t')(var.get('c'), var.get('u'))
PyJsHoisted_C_.func_name = 'C'
var.put('C', PyJsHoisted_C_)
@Js
def PyJsHoisted_B_(a, c, b, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b', 'c', 'd'])
    pass
    ((var.get('T').get('length')!=(Js(2.0)*var.get('a').get('length'))) and var.put('T', var.get('Array').create((Js(2.0)*var.get('a').get('length')))))
    var.get('r')(var.get('T'), Js(0.0))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('c').get('length')):
        (var.get('c').get(var.get('d')) and var.get('A')(var.get('T'), var.get('a'), var.get('c').get(var.get('d')), var.get('d')))
        # update
        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    var.get('C')(var.get('T'), var.get('b'))
    var.get('s')(var.get('a'), var.get('T'))
PyJsHoisted_B_.func_name = 'B'
var.put('B', PyJsHoisted_B_)
@Js
def PyJsHoisted_K_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'c', 'a'])
    pass
    #for JS loop
    var.put('b', var.get('a').get('length'))
    while ((Js(0.0)<var.get('b')) and var.get('a').get((var.get('b')-Js(1.0))).neg()):
        pass
        # update
        (var.put('b',Js(var.get('b').to_number())-Js(1))+Js(1))
    var.put('b', var.get('Array').create((var.get('b')+var.get('c'))))
    var.get('s')(var.get('b'), var.get('a'))
    return var.get('b')
PyJsHoisted_K_.func_name = 'K'
var.put('K', PyJsHoisted_K_)
@Js
def PyJsHoisted_F_(a, c, d, e, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'd':d, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'C', 'q', 'c', 'h', 'u', 'm', 'g', 'a', 't', 'e', 'd'])
    var.put('t', var.get('d').get('length'))
    var.put('C', var.get('c').get('length'))
    ((var.get('I').get('length')!=var.get('t')) and var.put('I', var.get('Array').create(var.get('t'))))
    #for JS loop
    var.get('r')(var.get('I'), Js(0.0))
    while ((Js(0.0)<var.get('t')) and (Js(0.0)==var.get('d').get((var.get('t')-Js(1.0))))):
        pass
        # update
        (var.put('t',Js(var.get('t').to_number())-Js(1))+Js(1))
    #for JS loop

    while ((Js(0.0)<var.get('C')) and (Js(0.0)==var.get('c').get((var.get('C')-Js(1.0))))):
        pass
        # update
        (var.put('C',Js(var.get('C').to_number())-Js(1))+Js(1))
    var.put('u', (var.get('I').get('length')-Js(1.0)))
    #for JS loop
    var.put('g', Js(0.0))
    while (var.get('g')<var.get('t')):
        var.put('q', (var.get('I').get('0')+(var.get('a').get(var.get('g'))*var.get('c').get('0'))))
        var.put('m', (((var.get('q')&var.get('H'))*var.get('e'))&var.get('H')))
        var.put('h', ((var.get('q')+(var.get('m')*var.get('d').get('0')))>>var.get('z')))
        var.put('q', var.get('a').get(var.get('g')))
        #for JS loop
        var.put('l', Js(1.0))
        while (var.get('l')<(var.get('C')-Js(4.0))):
            def PyJs_LONG_2_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('h', ((var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l'))))+(var.get('q')*var.get('c').get(var.get('l')))), '+'),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', ((var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l'))))+(var.get('q')*var.get('c').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', ((var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l'))))+(var.get('q')*var.get('c').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', ((var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l'))))+(var.get('q')*var.get('c').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', ((var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l'))))+(var.get('q')*var.get('c').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1)))
            PyJs_LONG_2_()

        #for JS loop

        while (var.get('l')<var.get('C')):
            PyJsComma(PyJsComma(PyJsComma(var.put('h', ((var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l'))))+(var.get('q')*var.get('c').get(var.get('l')))), '+'),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1)))

        #for JS loop

        while (var.get('l')<(var.get('t')-Js(4.0))):
            def PyJs_LONG_3_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('h', (var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l')))), '+'),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', (var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', (var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', (var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))),var.put('h', (var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l')))), '+')),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1)))
            PyJs_LONG_3_()

        #for JS loop

        while (var.get('l')<var.get('t')):
            PyJsComma(PyJsComma(PyJsComma(var.put('h', (var.get('I').get(var.get('l'))+(var.get('m')*var.get('d').get(var.get('l')))), '+'),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1)))

        #for JS loop

        while (var.get('l')<var.get('u')):
            PyJsComma(PyJsComma(PyJsComma(var.put('h', var.get('I').get(var.get('l')), '+'),var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))),var.put('h', var.get('z'), '>>')),(var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1)))

        var.get('I').put((var.get('l')-Js(1.0)), (var.get('h')&var.get('H')))
        # update
        (var.put('g',Js(var.get('g').to_number())+Js(1))-Js(1))
    if var.get('b')(var.get('d'), var.get('I')).neg():
        var.put('c', var.get('I'))
        var.put('l', (var.get('c').get('length') if (var.get('c').get('length')<var.get('d').get('length')) else var.get('d').get('length')))
        #for JS loop
        var.put('e', var.put('g', Js(0.0)))
        while (var.get('e')<var.get('l')):
            PyJsComma(PyJsComma(var.put('g', (var.get('c').get(var.get('e'))-var.get('d').get(var.get('e'))), '+'),var.get('c').put(var.get('e'), (var.get('g')&var.get('H')))),var.put('g', var.get('z'), '>>'))
            # update
            (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('e', var.get('l'))
        while (var.get('g') and (var.get('e')<var.get('c').get('length'))):
            PyJsComma(PyJsComma(var.put('g', var.get('c').get(var.get('e')), '+'),var.get('c').put(var.get('e'), (var.get('g')&var.get('H')))),var.put('g', var.get('z'), '>>'))
            # update
            (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    var.get('s')(var.get('a'), var.get('I'))
PyJsHoisted_F_.func_name = 'F'
var.put('F', PyJsHoisted_F_)
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
pass
pass
pass
pass
pass
pass
pass
pass
#for JS loop
var.put('z', Js(0.0))
var.put('H', Js(0.0))
var.put('N', (var.get('H')+Js(1.0)))
var.put('M', Js('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_=!@#$%^&*()[]{}|;:,.<>/?`~ \\\'"+-'))
var.put('z', Js(0.0))
while ((Js(1.0)<<(var.get('z')+Js(1.0)))>(Js(1.0)<<var.get('z'))):
    pass
    # update
    (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
var.put('z', (var.get('z')>>Js(1.0)))
var.put('H', ((Js(1.0)<<var.get('z'))-Js(1.0)))
var.put('N', (var.get('H')+Js(1.0)))
var.put('G', var.get('g')(Js(1.0), Js(1.0), Js(1.0)))
var.put('L', Js([]))
var.put('T', var.get('L'))
var.put('ha', var.get('L'))
var.put('pb', var.get('L'))
var.put('qb', var.get('L'))
var.put('Ea', var.get('L'))
var.put('Xa', var.get('L'))
var.put('I', var.get('L'))
@Js
def PyJs_anonymous_4_(a, b, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'v', 'M', 'A', 'a', 'b', 't', 'L', 'd'])
    var.put('a', var.get('h')(var.get('a'), var.get(u"this").get('Base')))
    var.put('b', var.get('h')(var.get('b'), var.get(u"this").get('Base')))
    var.put('d', var.get('h')(var.get('d'), var.get(u"this").get('Base')))
    var.put('l', var.get('a'))
    var.put('a', var.get('d').get('length'))
    var.put('a', var.get('g')(Js(0.0), ((var.get('l').get('length') if (var.get('l').get('length')>var.get('a')) else var.get('a'))*var.get('z')), Js(0.0)))
    var.get('s')(var.get('a'), var.get('l'))
    var.put('b', var.get('K')(var.get('b'), Js(2.0)))
    var.put('d', var.get('K')(var.get('d'), Js(2.0)))
    ((var.get('Xa').get('length')!=var.get('d').get('length')) and var.put('Xa', var.get('q')(var.get('d'))))
    if (Js(0.0)==(var.get('d').get('0')&Js(1.0))):
        var.get('s')(var.get('Xa'), var.get('a'))
        #for JS loop
        var.get('r')(var.get('a'), Js(1.0))
        while var.get('c')(var.get('b'), Js(0.0)).neg():
            ((var.get('b').get('0')&Js(1.0)) and var.get('B')(var.get('a'), var.get('Xa'), var.get('d')))
            var.get('u')(var.get('b'), Js(2.0))
            var.put('l', var.get('Xa'))
            var.put('v', var.get('d'))
            var.put('A', PyJsComma(Js(0.0), Js(None)))
            var.put('L', PyJsComma(Js(0.0), Js(None)))
            var.put('M', PyJsComma(Js(0.0), Js(None)))
            var.put('A', var.put('t', PyJsComma(Js(0.0), Js(None))))
            #for JS loop
            var.put('t', var.get('l').get('length'))
            while ((Js(0.0)<var.get('t')) and var.get('l').get((var.get('t')-Js(1.0))).neg()):
                pass
                # update
                (var.put('t',Js(var.get('t').to_number())-Js(1))+Js(1))
            var.put('A', ((Js(2.0)*var.get('t')) if (var.get('t')>var.get('v').get('length')) else (Js(2.0)*var.get('v').get('length'))))
            ((var.get('T').get('length')!=var.get('A')) and var.put('T', var.get('Array').create(var.get('A'))))
            var.get('r')(var.get('T'), Js(0.0))
            #for JS loop
            var.put('A', Js(0.0))
            while (var.get('A')<var.get('t')):
                var.put('M', (var.get('T').get((Js(2.0)*var.get('A')))+(var.get('l').get(var.get('A'))*var.get('l').get(var.get('A')))))
                var.get('T').put((Js(2.0)*var.get('A')), (var.get('M')&var.get('H')))
                var.put('M', var.get('z'), '>>')
                #for JS loop
                var.put('L', (var.get('A')+Js(1.0)))
                while (var.get('L')<var.get('t')):
                    PyJsComma(PyJsComma(var.put('M', ((var.get('T').get((var.get('A')+var.get('L')))+((Js(2.0)*var.get('l').get(var.get('A')))*var.get('l').get(var.get('L'))))+var.get('M'))),var.get('T').put((var.get('A')+var.get('L')), (var.get('M')&var.get('H')))),var.put('M', var.get('z'), '>>'))
                    # update
                    (var.put('L',Js(var.get('L').to_number())+Js(1))-Js(1))
                var.get('T').put((var.get('A')+var.get('t')), var.get('M'))
                # update
                (var.put('A',Js(var.get('A').to_number())+Js(1))-Js(1))
            var.get('C')(var.get('T'), var.get('v'))
            var.get('s')(var.get('l'), var.get('T'))

    else:
        var.get('r')(var.get('Xa'), Js(0.0))
        #for JS loop
        var.put('l', var.get('d').get('length'))
        while ((Js(0.0)<var.get('l')) and var.get('d').get((var.get('l')-Js(1.0))).neg()):
            pass
            # update
            (var.put('l',Js(var.get('l').to_number())-Js(1))+Js(1))
        var.put('v', var.get('N'))
        var.put('A', Js(0.0))
        #for JS loop
        var.put('t', (var.get('d').get('length')-Js(1.0)))
        while (Js(0.0)<=var.get('t')):
            var.put('A', (((var.get('A')*var.get('N'))+var.get('d').get(var.get('t')))%var.get('N')))
            # update
            (var.put('t',Js(var.get('t').to_number())-Js(1))+Js(1))
        var.put('v', var.get('e')(var.get('A'), var.get('N')), '-')
        var.get('Xa').put(var.get('l'), Js(1.0))
        var.get('B')(var.get('a'), var.get('Xa'), var.get('d'))
        (var.put('ha', var.get('q')(var.get('a'))) if (var.get('ha').get('length')!=var.get('a').get('length')) else var.get('s')(var.get('ha'), var.get('a')))
        #for JS loop
        var.put('l', (var.get('b').get('length')-Js(1.0)))
        while ((Js(0.0)<var.get('l'))&var.get('b').get(var.get('l')).neg()):
            pass
            # update
            (var.put('l',Js(var.get('l').to_number())-Js(1))+Js(1))
        if (Js(0.0)==var.get('b').get(var.get('l'))):
            var.get('r')(var.get('a'), Js(1.0))
        else:
            #for JS loop
            var.put('t', (Js(1.0)<<(var.get('z')-Js(1.0))))
            while (var.get('t') and (var.get('b').get(var.get('l'))&var.get('t')).neg()):
                pass
                # update
                var.put('t', Js(1.0), '>>')
            #for JS loop

            while 1:
                if var.put('t', Js(1.0), '>>').neg():
                    (var.put('l',Js(var.get('l').to_number())-Js(1))+Js(1))
                    if (Js(0.0)>var.get('l')):
                        var.get('F')(var.get('a'), var.get('G'), var.get('d'), var.get('v'))
                        break
                    var.put('t', (Js(1.0)<<(var.get('z')-Js(1.0))))
                var.get('F')(var.get('a'), var.get('a'), var.get('d'), var.get('v'))
                ((var.get('t')&var.get('b').get(var.get('l'))) and var.get('F')(var.get('a'), var.get('ha'), var.get('d'), var.get('v')))

    var.put('a', var.get('K')(var.get('a'), Js(1.0)))
    return var.put('a', var.get('m')(var.get('a'), var.get(u"this").get('Base')))
PyJs_anonymous_4_._set_name('anonymous')
@Js
def PyJs_anonymous_5_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'e', 'c', 'd'])
    pass
    var.put('b', (var.get('Math').callprop('floor', ((var.get('c')-Js(1.0))/var.get('z')))+Js(2.0)))
    var.put('b', var.get('g')(Js(0.0), Js(0.0), var.get('b')))
    pass
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('b').get('length')):
        var.get('b').put(var.get('d'), Js(0.0))
        # update
        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    var.put('e', (var.get('Math').callprop('floor', ((var.get('c')-Js(1.0))/var.get('z')))+Js(1.0)))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('e')):
        var.get('b').put(var.get('d'), var.get('Math').callprop('floor', (var.get('Math').callprop('random')*(Js(1.0)<<(var.get('z')-Js(1.0))))))
        # update
        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    var.get('b').put((var.get('e')-Js(1.0)), ((Js(2.0)<<((var.get('c')-Js(1.0))%var.get('z')))-Js(1.0)), '&')
    return var.get('m')(var.get('b'), var.get(u"this").get('Base'))
PyJs_anonymous_5_._set_name('anonymous')
var.put('Cb', Js({'Base':Js(10.0),'PowMod':PyJs_anonymous_4_,'RandomInt':PyJs_anonymous_5_}))
@Js
def PyJs_anonymous_6_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get('Cb').callprop('RandomInt', Js(64.0))
PyJs_anonymous_6_._set_name('anonymous')
@Js
def PyJs_anonymous_7_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('Cb').callprop('PowMod', Js('5'), var.get('a'), Js('791658605174853458830696113306796803'))
PyJs_anonymous_7_._set_name('anonymous')
@Js
def PyJs_anonymous_8_(a, c, this, arguments, var=var):
    var = Scope({'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a'])
    return var.get('Cb').callprop('PowMod', var.get('c'), var.get('a'), Js('791658605174853458830696113306796803'))
PyJs_anonymous_8_._set_name('anonymous')
var.put('mdh', Js({'prime':Js('791658605174853458830696113306796803'),'g':Js('5'),'gen_private':PyJs_anonymous_6_,'gen_public':PyJs_anonymous_7_,'gen_shared_secret':PyJs_anonymous_8_}))

pass


# Add lib to the module scope
mdh = var.to_python()