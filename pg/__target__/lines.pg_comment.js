'use strict';import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,__ipow__,
__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,filter,float,getattr,
hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";import{Statement}from"./statements.pg_statement.js";import{Mixin_Renderable}from"./mixins.pg_mixin_renderable.js";import{Mixin_Generatable}from"./mixins.pg_mixin_generatable.js";import{Decorator}from"./lines.pg_decorator.js";import{FR}from"./formula.pg_formula_requirement.js";
import{FP}from"./formula.pg_formula_pattern.js";import{FN}from"./formula.pg_formula_node.js";import{Expression}from"./expressions.pg_expression.js";import{COMMENT_LINES}from"./data.comments.comment_lines.js";import{JS_Random as R}from"./util.js_random.js";var __name__="lines.pg_comment";export var Comment=__class__("Comment",[Mixin_Generatable,Mixin_Renderable],{__module__:__name__,postfixes:["TODO","Not sure what this does","Yes this does work","foobar"],get get_patterns(){return __get__(this,function(self){if(arguments.length){var __ilastarg0__=
arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break}}}else;return[FP(FN(Statement),__kwargtrans__({reqs:FR("statements"),weight:4})),FP(FN(Expression),__kwargtrans__({reqs:FR("expressions"),weight:5})),FP(FN(Decorator),__kwargtrans__({reqs:FR("decorators"),weight:1}))]})},get generate(){return __get__(this,
function(self){if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break}}}else;if(R.flip_coin(.4))return self._generate_type_1();else if(R.flip_coin(.8))return self._generate_type_2();else return self._generate_type_3()})},get _generate_type_1(){return __get__(this,
function(self){if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break}}}else;var line=str(__super__(Comment,"generate")(self));return"# "+line})},get _generate_type_2(){return __get__(this,function(self){if(arguments.length){var __ilastarg0__=arguments.length-
1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break}}}else;if(R.flip_coin(.001))return"# TODO";else return R.choose_from(COMMENT_LINES)})},get _generate_type_3(){return __get__(this,function(self){if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=
arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break}}}else;var line=__super__(Comment,"generate")(self);return"{} # {}".format(line,R.choose_from(self.postfixes))})}});

//# sourceMappingURL=lines.pg_comment.map